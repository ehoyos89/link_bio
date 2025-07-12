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
                rx.flex(
                    rx.button("Volver al inicio", 
                              on_click=rx.redirect("/"), 
                              ),
                ),
            
                rx.heading(
                    "Automatización de infraestructura AWS con Terraform" \
                    " para aplicación Flask",
                    color="white",
                    size="8",
                    align="center",
                ),
                rx.text(
                    "Este proyecto implementa una solución de Infrastructure as Code (IaC)" \
                    " utilizando Terraform para automatizar el aprovisionamiento de recursos en AWS." \
                    " El objetivo es desplegar una aplicación CRUD desarrollada con Flask (Python)" \
                    " de manera eficiente y reproducible en la nube.", 
                    color="#cad3f5"
                ),
                rx.flex(
                    rx.heading(
                        "Arquitectura de la Aplicación",
                        weight="medium",
                        color="white",
                        size="6",
                        align="center",
                        width="100%",
                    ),
                    rx.image(
                        src="/FlaskApp.png",
                        alt="Arquitectura de la aplicación Flask",
                        max_width=styles.CONTENT_MAX_WIDTH,
                        width="100%",
                    ),
                    rx.text(
                        "La arquitectura para desplegar la aplicación en AWS incluye" \
                        " los siguientes componentes principales:",
                        color="#cad3f5",
                    ),
                    rx.list(
                        rx.list.item(
                            rx.icon("split", color="#fab387"),
                            " Application Load Balancer (ALB): Distribuye las solicitudes entrantes entre las instancias disponibles."),
                        rx.list.item(
                            rx.icon("arrow-up-narrow-wide", color="#fab387"),
                            " Auto Scaling Group: Gestiona automáticamente entre una y tres instancias EC2 según la demanda."),
                        rx.list.item(
                            rx.icon("package-open", color="#fab387"),
                            " Amazon S3: Almacena el contenido multimedia de la aplicación."),
                        rx.list.item(
                            rx.icon("database", color="#fab387"),
                            " Amazon RDS MySQL: Servidor de base de datos primario con una réplica en standby que se activa automáticamente en caso de falla."),
                    ),
                    direction="column",
                    spacing="2",
                ),
                rx.flex(
                    rx.heading(
                        "Diagrama de Red",
                        weight="medium",
                        color="white",
                        size="6",
                        align="center",
                        width="100%",
                    ),
                    rx.image(
                        src="/red.png",
                        alt="Diagrama de red para la aplicación Flask en AWS",
                        max_width=styles.CONTENT_MAX_WIDTH,
                        width="100%",
                    ),
                    rx.text(
                        "Las instancias EC2 se ubicarán en subredes públicas para" \
                        " permitir el acceso desde Internet a través del puerto 80 (HTTP)" \
                        " y del puerto 22 (SSH). En contraste, la base de datos se posicionará" \
                        " en subredes privadas y solo será accesible desde las instancias EC2" \
                        " mediante el puerto 3306 (MySQL).",
                        color="#cad3f5",
                    ),
                    direction="column",
                    spacing="2",
                ),
                rx.flex(
                    rx.heading(
                        "Configuración de NAT Gateway e Internet Gateway",
                        weight="medium",
                        color="white",
                        size="6",
                        align="center",
                        width="100%",
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
                    direction="column",
                    spacing="2",
                ),
                rx.image(
                    src="/flowlogs.png",
                    alt="Logo de Terraform",
                    max_width=styles.CONTENT_MAX_WIDTH,
                    width="100%",
                ),
                max_width=styles.CONTENT_MAX_WIDTH,
                #width="100%",
                spacing="6",
                margin_y=Size.MEDIUM.value,
                padding=Size.SMALL.value,
            )
        ),
        footer(),
    )
