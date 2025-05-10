import flet as ft

def main(page:ft.Page):
    #page.theme = "white"
    ola = ft.Text("Bora pra casa", size=200, color="red", bgcolor="white")
    page.add(ola)

ft.app(target=main)





