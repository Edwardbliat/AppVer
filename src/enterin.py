import flet as ft






def enterinpage(page: ft.Page):
    class EnterIn(ft.Column):
        def __init__(self):
            super().__init__()

            
        
        def buttom_registration(self, login_name, password):
            page.go(f"/mainpage/1")
            page.update()


            
        
            
        def build(self):
            self.login_name = ft.TextField(hint_text='Ваш логин...', width=300, border_color=ft.Colors.DEEP_PURPLE, border_width=3)
            self.password = ft.TextField(hint_text='Ваш пароль...', width=300, border_color=ft.Colors.DEEP_PURPLE, border_width=3)
            self.buttom_reg = ft.ElevatedButton(
                'Войти',
                bgcolor=ft.Colors.DEEP_PURPLE,
                color=ft.Colors.WHITE,
                height=70,
                width=200,
                on_click=lambda e: self.buttom_registration(self.login_name.value, self.password.value)
                )
            return ft.Column(controls=[
                self.login_name, 
                self.password, 
                self.buttom_reg,
                
                ],
                             horizontal_alignment=ft.CrossAxisAlignment.CENTER
                             )
    
    return ft.Column(
        controls=[
            ft.Image(src='intro3.jpg'),
            EnterIn(),
            ft.ElevatedButton('Вернуться к intro', on_click=lambda _: page.go("/")),
            
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        
    )