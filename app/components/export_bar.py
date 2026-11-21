"""Export bar region [G] for the dashboard skeleton."""

from dash import html


def create_export_bar() -> html.Div:
    """Return the export bar with a disabled CSV download placeholder."""
    return html.Div(
        id="region-export",
        className="export-bar",
        children=[
            html.Span("Export", className="export-label"),
            html.Button(
                "Download all filtered data (CSV)",
                id="download-all-csv-placeholder",
                className="placeholder-button",
                disabled=True,
                title="Placeholder — bulk CSV export will be added later",
            ),
        ],
    )
