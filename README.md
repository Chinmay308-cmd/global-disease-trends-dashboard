# Global Disease Trends Dashboard

An open-source interactive dashboard for exploring and visualizing global disease trends using public health data from the World Health Organization (WHO).

## Project Overview

The Global Disease Trends Dashboard aims to make public health information easier to explore and understand through interactive visualizations.

The project will support analysis of health indicators such as disease prevalence, incidence, and mortality across locations, age groups, sexes, and time periods, depending on the selected WHO dataset.

**Project objectives:**
- Collect and prepare public health datasets.
- Clean and validate data using Python.
- Store processed data in Parquet format.
- Develop interactive visualizations using Dash and Plotly.
- Enable comparisons of disease trends across geographical locations and demographic groups.
- Maintain reproducible data processing and documentation.

## Technology Stack

- **Programming Language:** Python 3.11
- **Data Processing:** Pandas, PyArrow
- **Dashboard:** Dash, Plotly
- **Testing:** pytest
- **Code Quality:** Ruff
- **Version Control:** Git and GitHub
- **Continuous Integration:** GitHub Actions

All direct dependency versions are pinned in `requirements.txt`.

## Project Structure

```text
global-disease-trends-dashboard/
├── app/                    # Dash application
├── scripts/                # Data download and preparation
├── data/
│   ├── raw/                # WHO raw snapshots (Git-ignored)
│   └── processed/          # Cleaned Parquet files
├── notebooks/              # Data inspection and analysis
├── tests/                  # Automated tests
├── docs/                   # Documentation
├── .github/
│   ├── workflows/
│   │   └── ci.yml
│   └── pull_request_template.md
├── .gitignore
├── .python-version
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

Install the following before setting up the project:

- Python 3.11
- Git
- pip
- Visual Studio Code (recommended)

### 1. Clone the Repository

Open the GitHub repository and select **Code → HTTPS** to copy its current clone URL.

```bash
git clone <repository-HTTPS-URL>
cd global-disease-trends-dashboard
```

The clone URL is intentionally not hard-coded because the repository will eventually be transferred to the CDF GitHub organization.

### 2. Create a Virtual Environment

**Windows (PowerShell)**

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If activation is blocked by PowerShell, use `.venv\Scripts\python.exe` directly when running Python commands.

**macOS**

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

Run the following command inside the activated virtual environment:

```bash
python -m pip install -r requirements.txt
```

This installs the pinned versions of Pandas, Dash, Plotly, PyArrow, pytest, and Ruff.

### 4. Run the Dashboard

The dashboard application is under development.

Once its entry point is implemented at `app/main.py`, run:

```bash
python app/main.py
```

Then open:

`http://127.0.0.1:8050/`

**Note:** The dashboard launch command will work only after the application entry point is added.

## Running Automated Tests

Run all project tests:

```bash
python -m pytest
```

An initial placeholder test is included to verify that the test environment and CI work correctly.

## Code Quality

This project uses Ruff for linting and formatting.

**Run linting:**

```bash
python -m ruff check .
```

**Check formatting:**

```bash
python -m ruff format --check .
```

**Automatically format Python files:**

```bash
python -m ruff format .
```

All checks must pass before a pull request can be merged.

## Continuous Integration

GitHub Actions automatically runs on every push and pull request.

The CI workflow:

1. Sets up Python 3.11.
2. Installs the required dependencies.
3. Runs Ruff linting.
4. Checks code formatting.
5. Runs pytest.

The required CI status check is `lint-and-test`.

## Contribution Guidelines

All team members must use feature branches and pull requests when contributing to the repository.

### Branch Naming Convention

Use the following format:

`<ticket-id>-short-description`

Example:

`931AA8-repo-setup`

### Contribution Process

1. Pull the latest changes from `main`.
2. Create a branch using the assigned ticket ID.
3. Make changes on the feature branch.
4. Run Ruff and pytest locally.
5. Commit and push the feature branch.
6. Open a pull request targeting `main`.
7. Complete the pull request template with:
   - What changed
   - Linked ticket ID
   - How it was tested
8. Request at least one approving review.
9. Ensure the required CI check passes.
10. Merge only after all requirements are satisfied.

Direct pushes to `main` are prohibited.

## Data Management and Git Exclusions

Original WHO datasets must be stored locally in:

`data/raw/`

The `data/raw/` directory is excluded through `.gitignore`.

**Never commit raw WHO CSV files or other source snapshots.**

Cleaned and validated datasets may be stored in:

`data/processed/`

Only commit processed datasets when their size, licensing, and project data policies permit it.

Do not commit secrets, API keys, or credentials.

## WHO Data Attribution

**Pending:** Insert the exact WHO attribution statement from the approved dataset report.

The attribution must be finalized before the repository setup ticket is closed.

## License

The project license is awaiting confirmation from the EPM.

Proposed options:

- MIT
- Apache-2.0

The official `LICENSE` file will be added once the EPM confirms the selected license.

## Repository Ownership and Transfer

This repository is temporarily hosted under a team member's personal GitHub account.

Once Community Dream Foundation (CDF) provides access to its GitHub organization, the existing repository will be transferred to the CDF organization.

The repository will be transferred rather than copied to preserve commit history, issues, and pull requests.

## Project Status

The initial repository structure, Python environment, dependency configuration, Ruff, pytest, and GitHub Actions CI have been established.

Data processing and interactive dashboard functionality will be developed in subsequent project tasks.
