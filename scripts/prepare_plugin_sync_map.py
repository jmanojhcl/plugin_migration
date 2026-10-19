import argparse
import csv
import json
from pathlib import Path
from urllib.parse import urlparse


def is_within(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
    except ValueError:
        return False
    return True


def load_mappings(csv_path: Path, repo_root: Path) -> list[dict[str, str]]:
    docs_root = (repo_root / "docs").resolve()
    mappings = []

    with csv_path.open(newline="", encoding="utf-8-sig") as csv_file:
        reader = csv.DictReader(csv_file)
        if not reader.fieldnames:
            raise ValueError("CSV is missing its header row")

        reader.fieldnames = [name.strip() for name in reader.fieldnames]
        required_fields = {"local_directory", "source_url"}
        if not required_fields.issubset(reader.fieldnames):
            raise ValueError("CSV must have local_directory and source_url columns")

        for line_number, row in enumerate(reader, start=2):
            local_directory = (row.get("local_directory") or "").strip()
            source_url = (row.get("source_url") or "").strip()
            target_directory = (repo_root / local_directory).resolve()
            parsed_url = urlparse(source_url)
            path_parts = parsed_url.path.rstrip("/").split("/")

            if (
                not local_directory
                or target_directory == docs_root
                or not is_within(target_directory, docs_root)
                or not target_directory.is_dir()
            ):
                raise ValueError(
                    f"CSV row {line_number}: local_directory must be an existing plugin folder under docs/"
                )

            if (
                parsed_url.scheme != "https"
                or parsed_url.hostname != "www.hcl-software.com"
                or len(path_parts) != 3
                or path_parts[1] != "plugins"
                or not path_parts[2]
            ):
                raise ValueError(
                    f"CSV row {line_number}: source_url must be an HCL plugin detail URL"
                )

            mappings.append(
                {
                    "local_directory": target_directory.relative_to(repo_root).as_posix(),
                    "source_url": source_url,
                }
            )

    if not mappings:
        raise ValueError("CSV contains no plugin mappings")

    return mappings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("output_path", type=Path)
    arguments = parser.parse_args()

    repo_root = Path.cwd().resolve()
    csv_path = (repo_root / arguments.csv_path).resolve()
    output_path = (repo_root / arguments.output_path).resolve()

    if not is_within(csv_path, repo_root) or not csv_path.is_file():
        parser.error("csv_path must name a file inside the repository")

    try:
        mappings = load_mappings(csv_path, repo_root)
    except ValueError as error:
        parser.error(str(error))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(mappings, indent=2) + "\n", encoding="utf-8")
    print(f"Validated {len(mappings)} plugin mapping(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())