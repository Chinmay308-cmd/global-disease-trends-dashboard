"""Chart and map panel placeholders for regions [C]–[F]."""

from dash import html

from app.components.filters import AGE_BANDS


def create_trend_panel() -> html.Section:
    """Return the trend chart placeholder for 2000–2024 [C]."""
    return _panel(
        region_id="region-trend",
        title="Trend chart",
        subtitle="2000–2024",
        body_children=[
            html.Div(
                className="chart-placeholder-body",
                children=[
                    html.P("Trend lines placeholder"),
                    html.P(
                        "Reserved space for WHO uncertainty bands",
                        className="reserve-note",
                    ),
                ],
            ),
        ],
    )


def create_world_map_panel() -> html.Section:
    """Return the world map placeholder for one selected year [D]."""
    return _panel(
        region_id="region-world-map",
        title="World map",
        subtitle="Selected year: 2024",
        body_children=[
            html.Div(
                className="chart-placeholder-body map-placeholder",
                children=[
                    html.P("Map canvas placeholder"),
                    html.Div(
                        className="map-legend-reserve",
                        children=[
                            html.Span("Colour legend reserve"),
                            html.Span(
                                "No estimate",
                                className="no-estimate-state",
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )


def create_age_sex_panel() -> html.Section:
    """Return the age and sex placeholder labelled 2024 only [E]."""
    return _panel(
        region_id="region-age-sex",
        title="Age and sex",
        subtitle="2024 only · Incidence case counts only",
        badge="2024",
        body_children=[
            html.Div(
                className="chart-placeholder-body",
                children=[
                    html.P("Age and sex breakdown placeholder"),
                    html.Ul(
                        className="age-band-list",
                        children=[html.Li(band) for band in AGE_BANDS],
                    ),
                ],
            ),
        ],
    )


def create_comparison_panel() -> html.Section:
    """Return the comparison placeholder for 2–4 locations [F]."""
    return _panel(
        region_id="region-comparison",
        title="Comparison",
        subtitle="Compare 2–4 countries or WHO regions",
        body_children=[
            html.Div(
                className="chart-placeholder-body",
                children=[
                    html.P("Comparison chart placeholder"),
                ],
            ),
        ],
    )


def _panel(
    *,
    region_id: str,
    title: str,
    subtitle: str,
    body_children: list,
    badge: str | None = None,
) -> html.Section:
    """Build a full-width stacked chart panel with PNG/CSV placeholders."""
    header_children: list = [html.H3(title, className="panel-title")]
    if badge is not None:
        header_children.append(html.Span(badge, className="panel-badge"))

    return html.Section(
        id=region_id,
        className="chart-panel",
        children=[
            html.Div(
                className="panel-header",
                children=[
                    html.Div(className="panel-heading", children=header_children),
                    html.P(subtitle, className="panel-subtitle"),
                    html.Div(
                        className="panel-actions",
                        children=[
                            html.Button(
                                "PNG",
                                className="placeholder-button export-button",
                                disabled=True,
                                title="Placeholder — PNG export will be added later",
                            ),
                            html.Button(
                                "CSV",
                                className="placeholder-button export-button",
                                disabled=True,
                                title="Placeholder — CSV export will be added later",
                            ),
                        ],
                    ),
                ],
            ),
            *body_children,
        ],
    )
