import streamlit.components.v1 as components
from pathlib import Path


def _resolve_graph_path(graph_path):

    path = Path(graph_path)

    if path.exists():
        return path

    backend_path = Path(__file__).resolve().parents[2] / "backend" / "app" / graph_path

    if backend_path.exists():
        return backend_path

    return path


def show_network(graph_path):

    graph_file = _resolve_graph_path(graph_path)

    with open(graph_file, "r", encoding="utf-8") as f:

        html = f.read()

    components.html(
        html,
        height=700,
        scrolling=True
    )