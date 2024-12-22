import reflex as rx
from link_bio.styles.styles import Size as Size

def footer() -> rx.Component:
  return rx.flex(
    rx.flex(
      rx.text("Sitio alojado en un 🪣 S3 de AWS"),
      rx.text("Powered by ", rx.link("Reflex", href="https://reflex.dev", is_external=True)),
      spacing="1",
      align="center",
      justify="center",
      width="100%",
      padding="1rem",
      color="gray",
      font_size="0.8rem",
    ),
    justify="center",
    align="center",
    width="100%",
    margin_bottom=Size.DEFAULT.value
  ) 
