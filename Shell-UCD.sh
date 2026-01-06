#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="${1:-.}"

find "$ROOT_DIR" -type f -name "downloads.md" | while read -r file; do
  echo "Updating: $file"

  sed -i \
    -e 's|https://raw.githubusercontent.com/UrbanCode/IBM-UCD-PLUGINS/main/files/|https://hclcr.io/files/devops/launch/plugins/launch-|g' \
    -e 's|\(https\?://[^ )]*\)ucd|\1launch|g' \
    "$file"
done

echo "Done."
