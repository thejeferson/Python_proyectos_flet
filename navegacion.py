
import flet
from flet import (
    AppBar,
    Icon,
    IconButton,
    Page,
    PopupMenuButton,
    PopupMenuItem,
    Text,
    colors,
    icons,
    Image
)

def main(page: Page):
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    page.appbar = AppBar(
        leading=Icon(icons.AUDIOTRACK),
        leading_width=40,
        title=Text(" Navegación"),
        center_title=True,
        bgcolor=colors.SURFACE_VARIANT,
        actions=[
            IconButton(icons.CALCULATE, tooltip="Cambiar a calculadora"),
            PopupMenuButton(tooltip="Páginas",
                items=[

                    PopupMenuItem( text="Login"),
                    PopupMenuItem(text="Item 2"),  # divider
                    PopupMenuItem(text="Item 3"),
                ]
            ),
        ],
    )
    page.add(Text("Aquí va el cuerpo!"))

flet.app(target=main, view=flet.WEB_BROWSER)