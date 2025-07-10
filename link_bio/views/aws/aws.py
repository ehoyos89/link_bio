import reflex as rx
import link_bio.styles.styles as styles
from link_bio.components.nav_bar import nav_bar
from link_bio.components.footer import footer
from link_bio.styles.styles import Size as Size
import link_bio.styles.styles as styles


def aws() -> rx.Component:
    return rx.box(
        nav_bar(),
        rx.center(
            rx.vstack(
                rx.heading(
                    "Automatización de infraestructura AWS con Terraform" \
                    " para aplicacion Flask",
                    color="white",
                    size="8",
                    align="center",
                ),
                rx.text(
                    "La automatización de infraestructura en la nube es " \
                    "una práctica esencial para el desarrollo ágil y la entrega " \
                    "continua.",
                    color="#cad3f5"
                ),
                rx.image(
                    src="/FlaskApp.png",
                    alt="Arquitectura de la aplicación Flask",
                    max_width=styles.CONTENT_MAX_WIDTH,
                    width="100%",
                ),
                rx.text(
                    "Este proyecto utiliza Terraform para definir y desplegar " \
                    "una aplicación Flask en AWS, incluyendo servicios como EC2, " \
                    "RDS y S3.",
                    color="#cad3f5",
                ),
                rx.image(
                    src="/red.png",
                    alt="Diagrama de red para la aplicación Flask en AWS",
                    max_width=styles.CONTENT_MAX_WIDTH,
                    width="100%",
                ),
                rx.text(
                    "El diagrama de red muestra cómo se conectan los " \
                    "diferentes componentes de la aplicación, incluyendo " \
                    "la base de datos y el almacenamiento.",
                    color="#cad3f5",
                ),
                rx.image(
                    src="/gateway.png",
                    alt="Logo de AWS",
                    max_width=styles.CONTENT_MAX_WIDTH,
                    width="100%",
                ),
                rx.text(
                    "AWS proporciona una plataforma robusta y escalable " \
                    "para desplegar aplicaciones web, y Terraform facilita " \
                    "la gestión de la infraestructura como código.",
                    color="#cad3f5",
                ),
                rx.image(
                    src="/flowlogs.png",
                    alt="Logo de Terraform",
                    max_width=styles.CONTENT_MAX_WIDTH,
                    width="100%",
                ),
                max_width=styles.CONTENT_MAX_WIDTH,
                width="100%",
                spacing="6",
                margin_y=Size.MEDIUM.value,
                padding=Size.SMALL.value,
            )
        ),
        footer(),
    )
