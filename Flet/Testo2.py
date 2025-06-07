import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    task_input = ft.TextField(hint_text="Digite uma tarefa", expand=True)
    task_list = ft.Column()

    def add_task(e):
        if task_input.value:
            task = ft.Row([
                ft.Text(task_input.value, expand=True),
                ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e: remove_task(e, task))
            ])
            task_list.controls.append(task)
            task_input.value = ""
            page.update()

    def remove_task(e, task):
        task_list.controls.remove(task)
        page.update()

    page.add(
        ft.Row([
            task_input,
            ft.ElevatedButton("Adicionar", on_click=add_task)
        ]),
        task_list
    )

ft.app(target=main,view=ft.WEB_BROWSER)
