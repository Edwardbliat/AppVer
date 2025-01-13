import flet as ft



def chatpage(page: ft.Page):


    return ft.Column(
        controls=[
            ft.Text('Это Чат'),
            ft.ElevatedButton('Вернуться к intro', on_click=lambda _: page.go("/")),
            
        ]
    )