import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size

def header() -> rx.Component:
  return rx.vstack(
    rx.hstack(
          rx.vstack(
            rx.avatar(
             fallback="EH",
             src="CloudLink.jpg", 
             high_contrast=True,
             size="7"
            ),
            align="center",
            padding="0.5rem",
          ),
          
          rx.vstack(
                rx.heading("Erick Hoyos", size="7", color="white"),
                rx.text("erick.hoyos@outlook.com", color="#8aadf4"),
                rx.hstack(
                  link_icon("github", "https://github.com/ehoyos89"),
                  link_icon("twitter", "https://x.com/HoyosErick89"),
                  # link_icon("instagram", "https://x.com/HoyosErick89"),
                  link_icon("linkedin", "https://www.linkedin.com/in/erick-sebastián-hoyos-arízaga-544a71339"),
                  align_items="start",
                ),
                spacing="1",      
          ),
    ),
    rx.text(
      """Ingeniero en Redes y Telecomunicaciones, con experiencia 
      en soporte de TI, diseño de soluciones en Amazon Web Services y desarrollo de scripts en Python 
      para automatización de tareas.""",
      color="#cad3f5",
    ),
    spacing="5",
    width="100%",
  )
