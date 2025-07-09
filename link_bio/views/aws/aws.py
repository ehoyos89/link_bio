import reflex as rx
import link_bio.styles.styles as styles
from link_bio.components.nav_bar import nav_bar
from link_bio.components.footer import footer
from link_bio.styles.styles import Size as Size

def aws() -> rx.Component:
    return rx.box(
        nav_bar(),
        rx.flex(
            rx.heading(
                """Automatización de infraestructura AWS con Terraform 
                para aplicación web""",
                size="7", 
                align="center"
            ),
            width="100%",
            padding=Size.MEDIUM.value,

            justify_content="center",
            align_items="center",
        ),
        rx.text(
            """Este proyecto demuestra cómo utilizar Terraform para automatizar la creación de una infraestructura en AWS 
            que aloja una aplicación web. Incluye la configuración de servicios como EC2, RDS y S3, 
            permitiendo un despliegue eficiente y escalable.""",
            color="#cad3f5",
            width="100%",
            padding=Size.MEDIUM.value,

        ),
        rx.image(
            src="/FlaskApp2.png",
            alt="CloudLink",
            width="100%",
            height="auto",
            padding=Size.MEDIUM.value,
            margin_y=Size.SMALL.value,
        ),
        footer()
    )
