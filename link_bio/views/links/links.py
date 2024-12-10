import reflex as rx
from link_bio.components.link_button import link_button 
from link_bio.components.title import title

def links() -> rx.Component:
  return rx.vstack(
    title("Mis proyectos"),
    link_button(
      "code",
      "Proyectos Python",
      "Web scraping, automatización y herramientas en general.",
      "https://github.com/ehoyos89",
      ),
    link_button(
      "cloud-cog",
      "Proyectos AWS", 
      "Diseños de arquitecturar para diferentes casos de uso.", 
      "https://github.com/ehoyos89",
      ),
    link_button(
      "network",
      "Proyectos Networking", 
      "Diseños de topologías de red avanzadas.", 
      "https://github.com/ehoyos89",
      ),
    link_button(
      "shield-check",
      "Proyectos Cyberseguridad", 
      "Ejercicios de pentesting y configuraciones de seguridad de red.", 
      "https://github.com/ehoyos89",
      ),
    link_button(
      "infinity",
      "Proyectos DevOps", 
      "Proyectos completos usando CI/CD e IaC.", 
      "https://github.com/ehoyos89",
      ),

    title("Mis certificaciones"),
    link_button(
      "cloud-cog",
      "AWS Solutions Architech Asociate",
      "Link de verificación.",
      "https://github.com/ehoyos89",
      ),
    link_button(
      "square-terminal",
      "Python Essentials PECP",
      "Link de verificación.",
      "https://github.com/ehoyos89",
      ),

    width="100%",
    spacing="6"
   )