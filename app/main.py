"""Dash application entry point for the Global Disease Trends Dashboard."""

from __future__ import annotations

import sys
from pathlib import Path

from dash import Dash

# Ensure the repository root is importable when launched via `python app/main.py`.
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from app.layout import create_layout  # noqa: E402

_ASSETS_FOLDER = Path(__file__).resolve().parent / "assets"

app = Dash(
    __name__,
    title="Global Disease Trends: Tuberculosis",
    assets_folder=str(_ASSETS_FOLDER),
    suppress_callback_exceptions=True,
)
server = app.server
app.layout = create_layout()


def main() -> None:
    """Start the local development server."""
    app.run(host="127.0.0.1", port=8050, debug=True)


if __name__ == "__main__":
    main()
