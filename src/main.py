import flet as ft
from introview import intropage
from enterin import enterinpage
from chat import chatpage



def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = 'TaskMe'
    page.window.width = 450
    page.window.height = 750
    page.scroll = ft.ScrollMode.ALWAYS

    
    def on_nav_change(e):
        if e.control.selected_index == 0:
            page.go(f"/mainpage/1")  # Главная страница
        elif e.control.selected_index == 1:
            page.go(f"/bookmark/1")  # Пример маршрута с "Закладкой"
        elif e.control.selected_index == 2:
            page.go(f"/calendar/1")
        elif e.control.selected_index == 3:
            page.go(f"/chat/1")
        page.update()
    
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    intropage(page),
                ],
            )
        )
        if page.route == "/enterin":
            page.views.append(
                ft.View(
                    '/enterin',
                    [
                        enterinpage(page)
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER
                    
                )
            )
        if page.route == (f"/chat/1"):
            page.views.append(
                ft.View(
                    "/chat/:id",
                    [
                        chatpage(page)
                    ],
                    navigation_bar=ft.NavigationBar(
                        destinations=[
                            ft.NavigationBarDestination(icon=ft.Icons.HOME, label='Главная'),
                            ft.NavigationBarDestination(icon=ft.Icons.BOOKMARK, label='Закладка'),
                            ft.NavigationBarDestination(icon=ft.Icons.CALENDAR_MONTH, label='Календарь'),
                            ft.NavigationBarDestination(icon=ft.Icons.CHAT, label='Чат'),
                        ],
                        selected_index=0,
                        on_change=on_nav_change,
                        adaptive=True,
            ),
                    scroll=ft.ScrollMode.ALWAYS,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go('/')

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, assets_dir='assets', upload_dir='assets/uploads', port=8000)