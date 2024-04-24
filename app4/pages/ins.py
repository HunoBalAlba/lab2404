from app4.templates import template

import reflex as rx


@template(route="/ins", title="Inscripciones")
def ins() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.heading("Inscripciones", size="8"),
        rx.text("Inscripcion"),
        rx.text(
            "En esta pagina encontrara incripciones docentes y estudiantes ",
            #rx.code("{your_app}/pages/ins.py"),
        ),
    )