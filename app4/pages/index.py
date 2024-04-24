"""The home page of the app."""

from app4 import styles
from app4.templates import template

import reflex as rx


#@template(route="/", title="Home", image="/github.svg")
@template(route="/", title="Inicio")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    
    with open("README.md", encoding="utf-8") as readme:
        content = readme.read()
    return rx.markdown(content, component_map=styles.markdown_style)
    
