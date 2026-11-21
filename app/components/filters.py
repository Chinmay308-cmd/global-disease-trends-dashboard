"""Filter sidebar region [B] for the dashboard skeleton."""

from dash import dcc, html

AGE_BANDS = [
    "0–4",
    "5–9",
    "10–14",
    "15–19",
    "20–24",
    "25–34",
    "35–44",
    "45–54",
    "55–64",
    "65+",
]


def create_filter_sidebar() -> html.Aside:
    """Return the fixed left filter sidebar with disabled placeholder controls."""
    return html.Aside(
        id="region-filters",
        className="filter-sidebar",
        children=[
            html.H2("Filters", className="sidebar-title"),
            html.P(
                "Placeholder controls — not functional yet",
                className="placeholder-note",
            ),
            _filter_group(
                label="Indicator",
                control=dcc.Dropdown(
                    id="filter-indicator",
                    options=[{"label": "Incidence", "value": "Incidence"}],
                    value="Incidence",
                    clearable=False,
                    disabled=True,
                    className="placeholder-control",
                ),
            ),
            _filter_group(
                label="Measure",
                control=dcc.Dropdown(
                    id="filter-measure",
                    options=[
                        {
                            "label": "Rate per 100,000",
                            "value": "Rate per 100,000",
                        }
                    ],
                    value="Rate per 100,000",
                    clearable=False,
                    disabled=True,
                    className="placeholder-control",
                ),
            ),
            _filter_group(
                label="Region",
                control=dcc.Dropdown(
                    id="filter-region",
                    options=[{"label": "All regions", "value": "All regions"}],
                    value="All regions",
                    clearable=False,
                    disabled=True,
                    className="placeholder-control",
                ),
            ),
            _filter_group(
                label="Country",
                control=dcc.Dropdown(
                    id="filter-country",
                    options=[{"label": "Global total", "value": "Global total"}],
                    value=["Global total"],
                    multi=True,
                    clearable=False,
                    disabled=True,
                    className="placeholder-control",
                ),
            ),
            _filter_group(
                label="Year range",
                control=dcc.RangeSlider(
                    id="filter-year-range",
                    min=2000,
                    max=2024,
                    step=1,
                    value=[2000, 2024],
                    marks={2000: "2000", 2024: "2024"},
                    disabled=True,
                    allowCross=False,
                    tooltip={"placement": "bottom", "always_visible": False},
                    className="placeholder-control",
                ),
            ),
            _filter_group(
                label="Map year",
                control=dcc.Dropdown(
                    id="filter-map-year",
                    options=[{"label": "2024", "value": 2024}],
                    value=2024,
                    clearable=False,
                    disabled=True,
                    className="placeholder-control",
                ),
            ),
            _filter_group(
                label="Age band",
                control=dcc.Dropdown(
                    id="filter-age-band",
                    options=[{"label": band, "value": band} for band in AGE_BANDS],
                    value=AGE_BANDS,
                    multi=True,
                    clearable=False,
                    disabled=True,
                    className="placeholder-control age-band-control",
                ),
            ),
            _filter_group(
                label="Sex",
                control=dcc.Dropdown(
                    id="filter-sex",
                    options=[{"label": "Both", "value": "Both"}],
                    value="Both",
                    clearable=False,
                    disabled=True,
                    className="placeholder-control",
                ),
            ),
            html.Button(
                "Reset filters",
                id="reset-filters-placeholder",
                className="placeholder-button reset-button",
                disabled=True,
                title="Placeholder — reset behaviour will be added later",
            ),
        ],
    )


def _filter_group(*, label: str, control) -> html.Div:
    """Wrap a labelled filter control."""
    return html.Div(
        className="filter-group",
        children=[
            html.Label(label, className="filter-label"),
            control,
        ],
    )
