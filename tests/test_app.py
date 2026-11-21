"""Smoke tests for the Dash app skeleton."""

from dash import Dash
from dash.development.base_component import Component

from app.components.footer import WHO_ATTRIBUTION
from app.main import app, server

REGION_IDS = {
    "region-header",
    "region-filters",
    "region-trend",
    "region-world-map",
    "region-age-sex",
    "region-comparison",
    "region-export",
    "region-footer",
}


def _collect_ids(
    component: Component | dict | list | str | int | float | None,
) -> set[str]:
    """Recursively collect component ids from a Dash layout tree."""
    found: set[str] = set()

    if component is None or isinstance(component, (str, int, float, bool)):
        return found

    if isinstance(component, list):
        for item in component:
            found.update(_collect_ids(item))
        return found

    if isinstance(component, dict):
        component_id = component.get("props", {}).get("id")
        if isinstance(component_id, str):
            found.add(component_id)
        found.update(_collect_ids(component.get("props", {}).get("children")))
        return found

    component_id = getattr(component, "id", None)
    if isinstance(component_id, str):
        found.add(component_id)

    children = getattr(component, "children", None)
    found.update(_collect_ids(children))
    return found


def test_app_imports_and_exposes_server() -> None:
    """The Dash app imports cleanly and exposes WSGI server for deployment."""
    assert isinstance(app, Dash)
    assert server is app.server


def test_layout_builds_without_errors() -> None:
    """The layout serializes and includes all eight wireframe regions."""
    layout = app.layout
    assert layout is not None

    serialized = layout.to_plotly_json()
    assert isinstance(serialized, dict)

    ids = _collect_ids(layout)
    assert REGION_IDS.issubset(ids)


def test_key_labels_are_present() -> None:
    """Required skeleton labels and attribution text are present in the layout."""
    text = str(app.layout.to_plotly_json())

    assert "Global Disease Trends: Tuberculosis (WHO data)" in text
    assert "2024" in text
    assert "Best viewed on a desktop" in text
    assert WHO_ATTRIBUTION in text
    assert "Provisional — pending #778C71" in text
    assert "11 November 2026" in text
    assert "16 November 2026" not in text
