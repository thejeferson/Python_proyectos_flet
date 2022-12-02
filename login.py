import flet
from flet import ElevatedButton, Page, Text, TextField, icons

def main(page: Page):
    def button_clicked(e):
        t.value = f"Textboxes values are:  '{tb1.value}', '{tb2.value}', '{tb3.value}', '{tb4.value}', '{tb5.value}'."
        page.update()

    t = Text()

    tb1 = TextField(label="Nombre", hint_text="Ingresa tu nombre aquí")
    tb2 = TextField(label="Apellido", hint_text="Ingresa tu apellido")
    tb3= TextField(label="Edad", hint_text="ingresa tu edad")
    b = ElevatedButton(text="Registrarme", on_click=button_clicked)
    page.add(tb1, tb2, tb3, b, t)

flet.app(target=main, view=flet.WEB_BROWSER)