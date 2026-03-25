import flet as ft



def main (page: ft.Page):
    page.title = "Soma de dois números"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = ft.Padding(20, 20, 20, 20)

    numero1 = ft.TextField(label="Número 1", keyboard_type=ft.KeyboardType.NUMBER, expand=True)
    numero2 = ft.TextField(label="Número 2", keyboard_type=ft.KeyboardType.NUMBER, expand=True)
    
    def somar():
        try:
            n1 = float(numero1.value)
            n2 = float(numero2.value)
            resultado.value = f"Resultado: {n1 + n2}"
        except ValueError:
            resultado.value = "Por favor, insira números válidos."
        page.update()
    
    def subtrair():
        try:
            n1 = float(numero1.value)
            n2 = float(numero2.value)
            resultado.value = f"Resultado: {n1 - n2}"
        except ValueError:
            resultado.value = "Por favor, insira números válidos."
        page.update()
        
    def multiplicar():
        try:
            n1 = float(numero1.value)
            n2 = float(numero2.value)
            resultado.value = f"Resultado: {n1 * n2}"
        except ValueError:
            resultado.value = "Por favor, insira números válidos."
        page.update()
        
    def dividir():
        try:
            n1 = float(numero1.value)
            n2 = float(numero2.value)
            if n2 != 0:
                resultado.value = f"Resultado: {n1 / n2}"
            else:
                resultado.value = "Não é possível dividir por zero."
        except ValueError:
            resultado.value = "Por favor, insira números válidos."
        page.update()
    
    botao_somar = ft.Button(content = ft.Text("Somar"), on_click=lambda _: somar())
    botao_subtrair = ft.Button(content = ft.Text("Subtrair"), on_click=lambda _: subtrair())
    botao_multiplicar = ft.Button(content = ft.Text("Multiplicar"), on_click=lambda _: multiplicar())
    botao_dividir = ft.Button(content = ft.Text("Dividir"), on_click=lambda _: dividir())
    
    resultado = ft.Text(value = "Resultado: ", size = 18, weight=ft.FontWeight.BOLD, expand=True, disabled=True)

    page.add(ft.Container(width=500, content=ft.Column(alignment=ft.MainAxisAlignment.CENTER, spacing=15, controls=[ft.Text("Calculadora", size=22, weight=ft.FontWeight.BOLD), ft.Row(controls=[numero1, numero2], spacing=10), ft.Row(controls=[botao_somar, botao_subtrair, botao_multiplicar, botao_dividir]), resultado]),))

ft.run(main)