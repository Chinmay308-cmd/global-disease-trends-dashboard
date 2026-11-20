"""Header region [A] for the dashboard skeleton."""

from dash import html


def create_header() -> html.Header:
    """Return the page header with title and About placeholder."""
    return html.Header(
        id="region-header",
        className="app-header",
        children=[
            html.H1(
                "Global Disease Trends: Tuberculosis (WHO data)",
                className="app-title",
            ),
            html.Button(
                "About",
                id="about-placeholder",
                className="placeholder-button",
                disabled=True,
                title="Placeholder — About content will be added later",
            ),
        ],
    )
