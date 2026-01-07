# HCL UCx Plugin Documentation

This repository contains the documentation for **HCL Plugins**. The documentation is written in Markdown and built using **MkDocs** static site generator.

There are two GitHub Actions workflows for publishing the documentation:

1. **Build docs and deploy to GitHub Pages** – runs automatically on pushes to the `main` branch.
2. **Deploy Docs to S3 (OIDC)** – a manual workflow that publishes the documentation to the production S3 bucket.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Updating Documentation Locally](#updating-documentation-locally)
- [Building and Previewing Locally](#building-and-previewing-locally)
- [GitHub Pages Deployment](#github-pages-deployment)
- [Production Deployment to S3](#production-deployment-to-s3)
- [Contributing](#contributing)

---

## Prerequisites

To work with this repository locally, you need the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [MkDocs](https://www.mkdocs.org/) (will be installed via pip)

---

## Updating Documentation Locally

1. Clone the repository:

	```bash
	git clone https://github.com/urbancode/HCL-UCx-PLUGIN-DOCS.git
	cd HCL-UCx-PLUGIN-DOCS
	```

2. Navigate to the `docs/` folder and update the Markdown files.

	If you need to add new pages:
	- Create a new `.md` file inside the `docs/` folder.
	- Update `mkdocs.yml` to include the new page in the navigation section.

---

## Building and Previewing Locally

1. Create a Python virtual environment (optional but recommended):

	```bash
	python -m venv venv
	# Activate the virtual environment
	# Windows:
	venv\Scripts\activate
	# Linux / macOS:
	source venv/bin/activate
	```

2. Install MkDocs and required plugins from `requirements.txt`:

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
   
   This will install MkDocs along with all necessary plugins and dependencies.

3. Build the site locally:

	```bash
	mkdocs build
	```
	This generates the static site in the `site/` folder.

4. Preview the documentation locally:

	```bash
	mkdocs serve
	```
	Open your browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

	Any changes you make to the Markdown files will automatically refresh in the browser.

---

## GitHub Pages Deployment

- **Workflow:** Build docs and deploy to GitHub Pages
- **Trigger:** Automatically runs on every push to the `main` branch.

**What it does:**

- Builds the MkDocs site
- Publishes the generated HTML to the `gh-pages` branch
- URL: [https://urbancode.github.io/HCL-UCx-PLUGIN-DOCS/](https://urbancode.github.io/HCL-UCx-PLUGIN-DOCS/)

Contributors do not need to manually push to `gh-pages`; the workflow handles this automatically.

---

## Production Deployment to S3

- **Workflow:** Deploy Docs to S3 (OIDC)
- **Trigger:** Manually started via the Actions tab
- **Purpose:** Publish the documentation to the production S3 bucket

**Steps:**

1. Go to the repository → Actions
2. Select the **Deploy Docs to S3 (OIDC)** workflow
3. Click **Run workflow** and select the branch (usually `main`)

**What it does:**

- Builds the MkDocs site
- Uses GitHub OIDC to assume the production AWS IAM role
- Syncs the `site/` folder to the S3 bucket

Only authorized users should trigger this workflow to publish to production.

---

## Contributing

1. Fork the repository and create a feature branch.
2. Make your documentation updates in Markdown inside the `docs/` folder.
3. Build and preview locally to verify changes.
4. Open a pull request targeting the `main` branch.

Once merged:

- GitHub Pages updates automatically via **Build docs and deploy to GitHub Pages**
- Production S3 deployment can be triggered manually via **Deploy Docs to S3 (OIDC)**

