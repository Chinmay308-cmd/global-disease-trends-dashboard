"""Top-level layout composition for the dashboard skeleton."""

from dash import html

from app.components import (
    create_age_sex_panel,
    create_comparison_panel,
    create_export_bar,
    create_filter_sidebar,
    create_footer,
    create_header,
    create_trend_panel,
    create_world_map_panel,
)


def create_layout() -> html.Div:
    """Compose the desktop-first skeleton covering regions [A]–[H]."""
    return html.Div(
        id="app-root",
        className="app-shell",
        children=[
            create_header(),
            html.Div(
                className="app-body",
                children=[
                    create_filter_sidebar(),
                    html.Main(
                        className="main-content",
                        children=[
                            create_trend_panel(),
                            create_world_map_panel(),
                            create_age_sex_panel(),
                            create_comparison_panel(),
                            create_export_bar(),
                        ],
                    ),
                ],
            ),
            create_footer(),
        ],
    )
