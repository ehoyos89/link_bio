import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size


def link_button(icon:str, tittle:str, body:str, url:str, is_external=True) -> rx.Component:
  return rx.link(
    rx.button(
      rx.hstack(
        rx.icon(icon, width="10%", height="10%"),
        rx.vstack(
          rx.text(tittle, style=styles.button_tittle_style),
          rx.text(body, style=styles.button_body_style),
          spacing="1",
          align_items="start",
          width="90%",
          height="90%"
        ),
        align="center",
        
      ),
    ),
    border_radius=Size.VERY_SMALL.value,
    border_width="1.5px",
    href=url,
    is_external=is_external,
    width="100%",
  )
