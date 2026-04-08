# Etapa 01 - Importação da biblioteca e definição do ponto de entrada
import flet as ft # Importa o framework Flet para construção da interface


def main(page: ft.Page): # Define a função principal que gerencia a sessão da página
    page.title = "Formulário com Tabela Responsiva" # Define o título da janela ou aba
    page.theme_mode = ft.ThemeMode.DARK # Configura o esquema de cores para o modo escuro
    page.bgcolor = "#0a0e27" # Define uma cor de fundo personalizada em hexadecimal
    page.padding = 20 # Define o espaçamento interno global da página
    page.scroll = ft.ScrollMode.AUTO # Habilita barra de rolagem automática se o conteúdo transbordar
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER # Alinha os componentes ao centro horizontalmente
    
    # Etapa 06
    dados_cadastrados = [] # Lista (array) para armazenar os registros em memória (simulando um BD)
    
    # Etapa 05 - Validações
    def validar_nome():
        # Verifica se há valor e se possui pelo menos 3 caracteres úteis
        valido = campo_nome.value and len(campo_nome.value.strip()) >= 3
        erro_nome.visible = not valido # Altera a visibilidade do aviso de erro conforme o booleano
        return valido

    def validar_email():
        email = campo_email.value or "" # Garante que o valor seja tratado como string
        # Validação básica de string para presença de '@' e '.' no domínio
        valido = "@" in email and "." in email.split("@")[-1]
        erro_email.visible = not valido
        return valido

    def validar_idade():
        try:
            idade = int(campo_idade.value) # Tenta converter a entrada para inteiro
            valido = 16 <= idade <= 120 # Define o intervalo permitido (regra de negócio)
        except: # Captura erros caso o usuário digite caracteres não numéricos
            valido = False
        erro_idade.visible = not valido
        return valido

    def validar_curso():
        # Validação de preenchimento mínimo para o campo curso
        valido = campo_curso.value and len(campo_curso.value.strip()) >= 3
        erro_curso.visible = not valido
        return valido

    def validar_formulario(e=None):
        # Agregador de validações: verifica se todos os campos retornam True
        valido = all([
            validar_nome(),
            validar_email(),
            validar_idade(),
            validar_curso()
        ])

        # Gerenciamento de estado do botão: habilita apenas se o formulário for válido
        botao_cadastrar.disabled = not valido
        botao_cadastrar.opacity = 1 if valido else 0.5 # Feedback visual de desabilitação
        page.update() # Atualiza a interface para refletir as mudanças de estado
        
    # Etapa 06
    def processar_formulario(e):
        # Insere um novo objeto (dicionário) na lista de persistência temporária
        dados_cadastrados.append({
            "nome": campo_nome.value,
            "email": campo_email.value,
            "idade": campo_idade.value,
            "curso": campo_curso.value
        })
        
        # Atualiza a string de feedback e a torna visível
        mensagem_sucesso.value = f"Cadastro realizado com sucesso! Total: {len(dados_cadastrados)}"
        mensagem_sucesso.visible = True
        
        # Etapa 07
        atualizar_tabela()

        limpar_campos() # Reseta o formulário após o sucesso
    
    # Etapa 04
    def limpar_campos(e=None):
        # Limpa o conteúdo (buffer) dos campos de texto
        campo_nome.value = ""
        campo_email.value = ""
        campo_idade.value = ""
        campo_curso.value = ""
        
        # Etapa 05
        erro_nome.visible = False
        erro_email.visible = False
        erro_idade.visible = False
        erro_curso.visible = False

        botao_cadastrar.disabled = True
        botao_cadastrar.opacity = 0.5
        
        # Etapa 04
        page.update() # Sincroniza as alterações com a interface do usuário
        
    # Etapa 07
    def atualizar_tabela():
        linhas_tabela.controls.clear() # Limpa a lista de widgets para evitar duplicação

        # Itera sobre os dados e cria novos widgets dentro de uma Row para cada registro
        for d in dados_cadastrados:
            linhas_tabela.controls.append(
                ft.Row(
                    spacing=20,
                    controls=[
                        ft.Text(d["nome"], width=150), # Define larguras fixas para simular colunas
                        ft.Text(d["email"], width=220),
                        ft.Text(d["idade"], width=80),
                        ft.Text(d["curso"], width=180),
                    ]
                )
            )

        tabela_container.visible = True # Exibe o container da tabela após o primeiro dado inserido
        page.update() # Renderiza a nova lista na tela
    
    
    # Etapa 02 - Campos                                      
    campo_nome = ft.TextField(
        label="Nome", width=400,
        # Etapa 05 
        on_change=validar_formulario) # Dispara a validação a cada tecla digitada
    # Etapa 05
    erro_nome = ft.Text("Nome mínimo de 3 caracteres.", color="#f44336", visible=False)
    
    # Etapa 02                                                                                
    campo_email = ft.TextField(
        label="Email", width=400, 
        keyboard_type=ft.KeyboardType.EMAIL, # Otimiza o teclado mobile para e-mail
        # Etapa 05
        on_change=validar_formulario)
    # Etapa 05
    erro_email = ft.Text("Email inválido.", color="#f44336", visible=False)
    
    # Etapa 02
    campo_idade = ft.TextField(
        label="Idade", width=400, 
        keyboard_type=ft.KeyboardType.NUMBER, # Otimiza o teclado mobile para números
        # Etapa 05
        on_change=validar_formulario)
    # Etapa 05
    erro_idade = ft.Text("Idade entre 16 e 120.", color="#f44336", visible=False)
    
    # Etapa 02
    campo_curso = ft.TextField(
        label="Curso", width=400,
        # Etapa 05
        on_change=validar_formulario)
    # Etapa 05
    erro_curso = ft.Text("Curso mínimo de 3 caracteres.", color="#f44336", visible=False)
    
    
    # Etapa 03 - Botões
    botao_cadastrar = ft.Button(
        content=ft.Text("Cadastrar"),
        disabled=True, # Estado inicial desabilitado (State management)
        opacity=0.5,
        # Etapa 06
        on_click=processar_formulario # Vincula o clique à função de processamento
    )

    botao_limpar = ft.Button(
        content=ft.Text("Limpar"),
        # Etapa 04
        on_click=limpar_campos # Vincula o clique à limpeza dos campos
    )
    
    # Etapa 06
    mensagem_sucesso = ft.Text(
        "", color="#66bb6a",
        weight=ft.FontWeight.BOLD,
        visible=False
    )
    
    # Coluna que servirá de container para os itens da tabela (suporta scroll)
    linhas_tabela = ft.Column(
        spacing=10,
        scroll=ft.ScrollMode.AUTO
    )

    # Etapa 07
    # Container interno da tabela (sem scroll horizontal)
    tabela_interna = ft.Container(
        height=250, # Define uma altura fixa para a área de dados
        padding=10,
        border_radius=10,
        bgcolor="#1a1a2e",
        border=ft.Border.all(1, "#33ffff"), # Borda sutil para delimitação
        content=ft.Column(
            controls=[
                ft.Text("Usuários Cadastrados", size=18, weight=ft.FontWeight.BOLD),
                ft.Column(
                    controls=[
                        # Cabeçalho da tabela com labels em negrito
                        ft.Row(
                            spacing=20,
                            controls=[
                                ft.Text("Nome", width=150, weight=ft.FontWeight.BOLD),
                                ft.Text("Email", width=220, weight=ft.FontWeight.BOLD),
                                ft.Text("Idade", width=80, weight=ft.FontWeight.BOLD),
                                ft.Text("Curso", width=180, weight=ft.FontWeight.BOLD),
                            ]
                        ),
                        ft.Divider(), # Linha separadora horizontal
                        linhas_tabela # Local onde as linhas dinâmicas serão injetadas
                    ]
                )
            ]
        )
    )

    # Container externo com scroll horizontal (Garante responsividade em telas menores)
    tabela_container = ft.Container(
        visible=False,
        content=ft.Row(
            scroll=ft.ScrollMode.AUTO,
            controls=[tabela_interna]
        )
    )

    # Etapa 01
    # Título da aplicação e montagem da árvore de widgets
    page.add(
        ft.Column(
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("Formulário de Cadastro", size=22, weight=ft.FontWeight.BOLD),
                
                # Etapa 02   Etapa 05
                campo_nome, erro_nome,
                campo_email, erro_email,
                campo_idade, erro_idade,
                campo_curso, erro_curso,
                
                # Etapa 06
                mensagem_sucesso,
                
                # Etapa 03
                ft.Row(
                    spacing=15,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[botao_limpar, botao_cadastrar]
                ),
                
                # Etapa 07
                tabela_container
            ]
        )
    )

# Inicializa o app chamando a função main
ft.run(main)
