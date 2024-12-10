"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from link_bio.components.nav_bar import nav_bar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.footer import footer
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size


# class State(rx.State):
#    pass
#   """The app state."""


def index() -> rx.Component:
    return rx.box(
            nav_bar(),
            rx.center(
                rx.vstack(
                    header(),
                    links(),
                    max_width=styles.MAX_WIDTH, 
                    width="100%",
                    margin_y=Size.MEDIUM.value,
                    padding=Size.SMALL.value,     
                ),
            ),
        footer()
    )


app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)
app._compile()