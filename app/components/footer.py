"""Footer region [H] for the dashboard skeleton."""

from dash import html

# Keep attribution in one constant so ticket #778C71 can update it in one place.
# Ticket #AE34BB requires 11 November 2026 (not the wireframe draft's 16 November).
WHO_ATTRIBUTION = (
    "Source: World Health Organization, Global Tuberculosis Programme. "
    "Global TB database, data to 2024, downloaded 11 November 2026. "
    "Underlying data provided by countries to WHO."
)

PROVISIONAL_NOTE = "Provisional — pending #778C71"


def create_footer() -> html.Footer:
    """Return the page footer with provisional WHO attribution and placeholders."""
    return html.Footer(
        id="region-footer",
        className="app-footer",
        children=[
            html.P(WHO_ATTRIBUTION, className="footer-attribution"),
            html.P(PROVISIONAL_NOTE, className="footer-provisional"),
            html.Div(
                className="footer-links",
                children=[
                    html.Button(
                        "Data notes",
                        id="data-notes-placeholder",
                        className="placeholder-button footer-link-button",
                        disabled=True,
                        title="Placeholder — data notes will be added later",
                    ),
                    html.Button(
                        "Repo",
                        id="repo-placeholder",
                        className="placeholder-button footer-link-button",
                        disabled=True,
                        title="Placeholder — repository link will be added later",
                    ),
                ],
            ),
            html.P(
                "Best viewed on a desktop",
                className="footer-desktop-note",
            ),
        ],
    )
