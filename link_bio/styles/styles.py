import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor

class Size(Enum):
  VERY_SMALL = "0.5em"
  SMALL = "1em"
  DEFAULT = "1.5em"
  MEDIUM = "1.8em"
  BIG = "3em"

#Constants
MAX_WIDTH = "600px"

# Estilo global
BASE_STYLE = {
  "background_color": Color.BACKGROUND.value,
  rx.button: {
    "width" : "100%",
    "height" : "100%",
    "display" : "block",
    "padding" : Size.SMALL.value,
    "text_align" : "start",
    "border_radius" : Size.VERY_SMALL.value,
    "background_color" : Color.CONTENT.value,
    "_hover" : {
      "background_color" : Color.SECONDARY.value
    }
  }
}

# Estilos a nivel de objeto
button_tittle_style = dict(
  font_size=Size.DEFAULT.value,
  font_family="Montserrat",
  font_weight="bold",
  color="white",
)
navbar_title_style = dict(
  font_size=Size.DEFAULT.value,
  font_family="JetBrains Mono",
  color="#181926",
)
button_body_style = dict(
  font_size=Size.SMALL.value,
  font_family="JetBrains Mono",
  font_weight="regular",
  color="white",
)

title_style = dict(
  width="100%",
  font_size=Size.MEDIUM.value,
  font_family="Montserrat",
  padding_top=Size.SMALL.value
)

