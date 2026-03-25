import flet as ft

def main(page: ft.Page):
    page.title = "Semana 1 = Hello Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#06095E"
    page.padding = ft.Padding(left=20, top=20, right=20, bottom=20)
    page.scroll = ft.ScrollMode.AUTO

    container_cabecalho = ft.Container(
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
            controls=[
                ft.Container(
                    content=ft.Text("🚀", size=60,),
                    padding=10
                ),
                ft.Text("Bem-vindo à Semana 1 do curso de Flet", size=20, weight=ft.FontWeight.BOLD, color="#FFFFFF", text_align=ft.TextAlign.CENTER),
                ft.Text("Desenvolvimento de Aplicativos Python", color="#FFFFFF", text_align=ft.TextAlign.CENTER)
            ]
        ),
        padding=20,
        border_radius=20,
        gradient=ft.LinearGradient(begin=ft.alignment.Alignment(-1, -1), end=ft.alignment.Alignment(1, 1), colors=["#FF0000", "#0000FF"]),
    
        border=ft.border.all(1, "#2178D5")
    
    )

    cartao_informativo = ft.Container(
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
            controls=[
                ft.Row(alignment=ft.MainAxisAlignment.CENTER, spacing=10, controls=[
                    ft.Text("📅", size=20),
                    ft.Text("Semana 1", size=14, weight=ft.FontWeight.BOLD, color="#FFFFFF")
                ]),
                ft.Row(alignment=ft.MainAxisAlignment.CENTER, spacing=10, controls=[
                    ft.Text("🎓", size=20),
                    ft.Text("7º fase de Computação", size=14, weight=ft.FontWeight.BOLD, color="#FFFFFF")
                ])
            ]
        ),
        padding=15,
        border_radius=15,
        bgcolor="#1E1E1E",
        border=ft.border.all(1, "#2178D5")
    )

    page.add(ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=20,
        controls=[
            container_cabecalho,
            cartao_informativo
        ]
    ))

ft.run(main)