import flet as ft
from flet.auth.providers import GitHubOAuthProvider


def intropage(page: ft.Page):
    def text_for_present():
        return ft.Column(
            controls=[
                ft.Text(
                    'Управляй своими задачами',
                    theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                    weight=ft.FontWeight.W_600
                    ),
                ft.Text(
                    'Для личного пользования, семьи и команды своего проекта с индивидуальным решением',
                    max_lines=3,
                    width=350,
                    height=60
                    )
                ],
            alignment=ft.MainAxisAlignment.START
            )
    
    def image_for_present():    
        return ft.Row(
            scroll=True,
            width=400,
            height=300,
            wrap=False,
            controls=[
                ft.Image(
                    src='intro.jpg',
                    width=400,
                    height=300,
                    fit=ft.ImageFit.CONTAIN
                    ),
                ft.Image(
                    src='intro2.jpg',
                    width=400,
                    height=300,
                    fit=ft.ImageFit.CONTAIN
                    ),
                ft.Image(
                    src='intro3.jpg',
                    width=400,
                    height=300,
                    fit=ft.ImageFit.CONTAIN
                    )
                ]
            )
    
    #Кнопки входа
    def buttom_enter():
        return ft.Row(
            controls=[
                ft.ElevatedButton(
                    text='Зарегистрироваться',
                    bgcolor=ft.Colors.INDIGO_800,
                    color=ft.Colors.WHITE,
                    width=200,
                    height=50,
                    on_click= lambda _: page.go('/registration'),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    
    #load_dotenv('TaskMeApp\assets\client')
    #os.getenv("GITHUB_CLIENT_ID")
    #os.getenv("GITHUB_CLIENT_SECRET")
    GITHUB_CLIENT_ID = 'Ov23liQ2z5uvWnBPw5hk'
    GITHUB_CLIENT_SECRET = '027fc5f8dfe9808baa3ef1408625501d365ca57e'

    provider = GitHubOAuthProvider(
        client_id=GITHUB_CLIENT_ID,
        client_secret=GITHUB_CLIENT_SECRET,
        redirect_url="https://localhost:8000/api/oauth/redirect",
    )
    
    def login_click(e):
        page.login(provider)

    def on_login(e):
        print("Login error:", e.error)
        print("Access token:", page.auth.token.access_token)
        print("User ID:", page.auth.user.id)

    page.on_login = on_login
    

    
    
    return ft.Column(
        controls=[
            image_for_present(),
            text_for_present(),
            ft.ElevatedButton(text = 'Войти',
                              on_click=lambda _: page.go('/enterin'), 
                              bgcolor=ft.Colors.INDIGO_800, 
                              color='WHITE',
                              width=200,
                              height=50),
            buttom_enter(),
            ft.ElevatedButton("Login with GitHub", on_click=login_click,
                              bgcolor=ft.Colors.INDIGO_800, 
                              color='WHITE',
                              width=200,
                              height=50),
            ft.ElevatedButton('Зайти через Телеграм',
                              bgcolor=ft.Colors.INDIGO_800, 
                              color='WHITE',
                              width=200,
                              height=50,
                              url='https://t.me/TaskMeApp_bot',
                              )
            
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.ADAPTIVE
    )
    
