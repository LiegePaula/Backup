import flet as ft

def main(page: ft.Page):
    page.title = "Meu Web App com Flet"
    page.theme_mode = ft.ThemeMode.LIGHT  # Pode alternar para DARK se preferir
    page.bgcolor = "#F5F5F5"
    
    # Cabeçalho estilizado
    header = ft.Container(
        content=ft.Text("Bem-vindo ao Meu Web App", size=24, weight=ft.FontWeight.BOLD),
        alignment=ft.alignment.center,
        padding=10,
        bgcolor="#007BFF",
        border_radius=10,
        margin=10,
    )
    
    # Campo de entrada e botão
    input_field = ft.TextField(label="Digite algo", width=300)
    result_text = ft.Text("Resultado aparecerá aqui", size=16)
    
    def on_click(e):
        result_text.value = f"Você digitou: {input_field.value}"
        page.update()
    
    button = ft.ElevatedButton("Enviar", on_click=on_click, bgcolor="#007BFF", color="white")
    
    # Layout
    content = ft.Column([
        header,
        input_field,
        button,
        result_text
    ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    
    page.add(content)
    
ft.app(target=main, view=ft.WEB_BROWSER)




