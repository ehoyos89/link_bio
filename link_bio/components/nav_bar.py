import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size

def nav_bar() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.icon(tag="coffee"),
                    bg="#8aadf4",
                    padding=Size.VERY_SMALL.value,
                    border_radius=Size.VERY_SMALL.value,
                
                ),
                rx.box(
                    rx.hstack(
                        rx.icon(tag="square-terminal", color="black"),
                        rx.text("bash",
                            color="#181926",
                            ),
                        bg="#91d7e3",
                        padding=Size.VERY_SMALL.value,
                        border_radius=Size.VERY_SMALL.value
                    ),
                ),
                rx.box(
                    rx.hstack(
                        rx.icon(tag="user-round", color="black"),
                        rx.text(
                            "ehoyos/",
                                color="#181926",
                            ),
                        bg="#f5a97f",
                        padding=Size.VERY_SMALL.value,
                        border_radius=Size.VERY_SMALL.value
                    )
                ),
                rx.box(
                    rx.hstack(
                        rx.icon(tag="split", color="black"),
                        rx.text("main",
                                color="#181926", 
                                ),
                        bg="#eed49f",
                        padding=Size.VERY_SMALL.value,
                        border_radius=Size.VERY_SMALL.value
                    )
                ),
                spacing="0",

            ),
            rx.hstack(
                rx.icon(tag="chevron-right", color="#8aadf4"),
                rx.text(
                    "cowsay \"Bienvenido\"",
                    color="#cad3f5",
                ),
            ),     
        ),
        position="sticky",
        padding_x=Size.SMALL.value,
        padding_y=Size.SMALL.value,
        width="100%",
        align="start",
        z_index="999",
        top="0",
        bg="#1e2030"
    )
