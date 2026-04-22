"""
Painel de Finanças Pessoais
Objetivo Didático: Demonstrar CRUD em memória, Layout Responsivo e Gerenciamento de Estado.
Framework: Flet (Python)

CONCEITOS ABORDADOS NESTE ARQUIVO:
  - Variáveis globais e listas como banco de dados em memória
  - Funções auxiliares (helpers) com Generator Expressions
  - Formatação de strings com f-string e formatação de moeda
  - Componentização de widgets (fábrica de cartões)
  - CRUD: Create (salvar), Read (atualizar_tela)
  - Validação de dados com try/except e ValueError
  - Layout responsivo com ResponsiveRow
  - Reatividade manual: limpar e repopular listas na tela
  - Gráfico de barras simulado com Containers proporcionais
"""

# ------------------------------------------------------------------------------
# IMPORTAÇÕES
# ------------------------------------------------------------------------------
# "import flet as ft" carrega a biblioteca Flet com o apelido "ft".
# Flet transforma código Python em interfaces gráficas usando widgets do Flutter.
import flet as ft

# "from datetime import datetime" importa apenas a classe datetime do módulo
# datetime. Isso evita escrever "datetime.datetime.now()" — basta "datetime.now()".
from datetime import datetime


# ==============================================================================
# CAMADA DE MODELO — Armazenamento de Dados em Memória
# ==============================================================================
# Em aplicações reais, os dados ficam em bancos de dados (SQLite, PostgreSQL...).
# Aqui, usamos uma lista Python como substituto didático — os dados existem
# apenas enquanto o programa está rodando e são perdidos ao fechar o app.
#
# Por que lista global e não dentro de main()?
#   Uma lista global pode ser acessada e modificada por qualquer função do módulo.
#   Em projetos maiores, prefira encapsular em classes ou camadas de serviço.
# ==============================================================================

# Lista que armazena as transações. Cada transação será um dicionário Python.
# Começa vazia [] e vai crescendo a cada chamada de salvar().
transacoes = []

# Tupla de strings com as categorias disponíveis nos menus de seleção.
# Usamos uma lista (poderia ser tupla) para facilitar iteração com list comprehension.
# Adicionar uma nova categoria aqui reflete automaticamente no Dropdown da tela.
CATEGORIAS = ["Alimentação", "Transporte", "Moradia", "Saúde", "Lazer", "Salário", "Outros"]


# ==============================================================================
# CAMADA DE LÓGICA DE NEGÓCIO — Funções Auxiliares (Helpers)
# ==============================================================================
# Separar cálculos e formatações em funções próprias (fora de main) tem
# duas vantagens:
#   1. Reutilização: qualquer parte do código pode chamar essas funções
#   2. Testabilidade: funções puras (sem dependência de UI) são fáceis de testar
# ==============================================================================


# ------------------------------------------------------------------------------
# FUNÇÃO: calcular_saldo()
# ------------------------------------------------------------------------------
# Percorre a lista "transacoes" e soma valores de entradas e saídas separadamente.
#
# CONCEITO — Generator Expression:
#   "sum(t["valor"] for t in transacoes if t["tipo"] == "Entrada")"
#   é equivalente ao loop abaixo, porém mais compacto e eficiente:
#
#     total = 0
#     for t in transacoes:
#         if t["tipo"] == "Entrada":
#             total += t["valor"]
#
#   A Generator Expression não cria uma lista intermediária em memória —
#   ela "gera" cada valor sob demanda, o que é mais econômico para listas grandes.
#
# Retorno: tupla com três floats (entradas, saidas, saldo)
# ------------------------------------------------------------------------------
def calcular_saldo():
    # Soma todos os valores onde o campo "tipo" do dicionário é "Entrada"
    entradas = sum(t["valor"] for t in transacoes if t["tipo"] == "Entrada")

    # Soma todos os valores onde o campo "tipo" do dicionário é "Saída"
    saidas   = sum(t["valor"] for t in transacoes if t["tipo"] == "Saída")

    # Retorna uma TUPLA com três valores de uma vez.
    # Quem chamar esta função pode desempacotar: e, s, saldo = calcular_saldo()
    return entradas, saidas, entradas - saidas


# ------------------------------------------------------------------------------
# FUNÇÃO: formatar(valor)
# ------------------------------------------------------------------------------
# Converte um número float para string no formato monetário brasileiro.
#
# CONCEITO — Formatação de números com f-string:
#   f"{valor:,.2f}" usa a mini-linguagem de formatação do Python:
#     ,   → separador de milhar com vírgula (ex: 1,234.56)
#     .2f → float com exatamente 2 casas decimais
#
#   Resultado para valor=1234.5: "R$ 1,234.50"
#   Nota: o separador de milhar aqui é "," (padrão inglês). Em produção,
#   use o módulo "locale" para formatação conforme o idioma do sistema.
#
# Parâmetro: valor (float) — número a ser formatado
# Retorno:   string no formato "R$ X,XXX.XX"
# ------------------------------------------------------------------------------
def formatar(valor):
    return f"R$ {valor:,.2f}"


# ==============================================================================
# CAMADA DE INTERFACE — View e Controller
# ==============================================================================
# No Flet, toda a interface e lógica de interação ficam dentro de main(page).
# "page" é o objeto que representa a janela do aplicativo — passado pelo Flet.
# ==============================================================================
def main(page: ft.Page):

    # --------------------------------------------------------------------------
    # CONFIGURAÇÕES INICIAIS DA PÁGINA
    # --------------------------------------------------------------------------

    # Título exibido na barra de título do sistema operacional / aba do navegador
    page.title = "Finanças Pessoais"

    # Cor de fundo da janela em hexadecimal. "#1e1e2e" é um azul-escuro profundo.
    # Cores hex: #RRGGBB onde RR=vermelho, GG=verde, BB=azul (cada par: 00 a FF)
    page.bgcolor = "#1e1e2e"

    # Espaçamento interno entre a borda da janela e os widgets (em pixels)
    page.padding = 16

    # ScrollMode.AUTO: adiciona barra de rolagem vertical automaticamente
    # quando o conteúdo da página excede a altura disponível da janela.
    page.scroll = ft.ScrollMode.AUTO


    # --------------------------------------------------------------------------
    # DESIGN SYSTEM — Variáveis de Estilo Centralizadas
    # --------------------------------------------------------------------------
    # Centralizar cores e estilos em variáveis tem duas vantagens:
    #   1. Consistência: todos os campos usam exatamente a mesma cor
    #   2. Manutenção: mudar a cor de todos os campos = alterar 1 variável
    #
    # Em projetos maiores, isso evolui para um arquivo de tema separado.
    # --------------------------------------------------------------------------

    # Cor de fundo dos campos de entrada — azul escuro quase preto
    CAMPO_BG  = "#13131f"

    # Cor do texto digitado nos campos — branco puro
    CAMPO_COR = "white"

    # ft.TextStyle: objeto que define aparência de texto (cor, tamanho, peso, etc.)
    # Usado em label_style (rótulo do campo) e hint_style (placeholder)
    LABEL_COR = ft.TextStyle(color="#b0b0cc", size=13)  # cinza-azulado claro, 13px
    HINT_COR  = ft.TextStyle(color="#555577")            # cinza-azulado escuro

    # Cor das bordas dos campos — roxo médio
    BORDA = "#6c63ff"


    # --------------------------------------------------------------------------
    # COMPONENTES DE ENTRADA (INPUT WIDGETS)
    # --------------------------------------------------------------------------
    # Criamos os widgets de entrada FORA do layout (page.add) para podermos
    # acessar seus valores (.value) dentro dos handlers como salvar().
    # Se fossem criados diretamente no layout, não teríamos referência a eles.
    # --------------------------------------------------------------------------

    # Campo de texto para a descrição da transação
    campo_desc = ft.TextField(
        label="Descrição",                          # rótulo flutuante acima do campo
        hint_text="Ex: Almoço, Ônibus, Conta de luz...", # texto de exemplo (placeholder)
        bgcolor=CAMPO_BG,                           # cor de fundo do campo
        color=CAMPO_COR,                            # cor do texto digitado
        border_color=BORDA,                         # cor da borda quando não focado
        focused_border_color="#a09af0",             # cor da borda quando o campo está ativo
        label_style=LABEL_COR,                      # estilo do rótulo
        hint_style=HINT_COR,                        # estilo do placeholder
        border_radius=8,                            # cantos arredondados da borda
    )

    # Campo de texto para o valor monetário da transação
    campo_valor = ft.TextField(
        label="Valor (R$)",
        hint_text="Ex: 35.50",
        bgcolor=CAMPO_BG,
        color=CAMPO_COR,
        border_color=BORDA,
        focused_border_color="#a09af0",
        label_style=LABEL_COR,
        hint_style=HINT_COR,
        border_radius=8,
        # KeyboardType.NUMBER: sugere ao sistema operacional abrir teclado numérico
        # em dispositivos móveis (celular/tablet). No desktop não tem efeito visual.
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    # Dropdown: componente de seleção com lista suspensa (como <select> no HTML)
    # O usuário clica e escolhe uma das opções definidas em "options"
    campo_tipo = ft.Dropdown(
        label="Tipo",
        color="white",                  # cor do texto da opção selecionada
        bgcolor=CAMPO_BG,               # cor de fundo do dropdown
        border_color=BORDA,
        focused_border_color="#a09af0",
        label_style=LABEL_COR,
        border_radius=8,
        options=[
            # ft.dropdown.Option: define cada item da lista suspensa
            # key   = valor interno que vai para campo_tipo.value ao selecionar
            # text  = texto exibido na lista (fallback)
            # content = widget customizado exibido na opção (permite cor personalizada)
            ft.dropdown.Option(
                key="Entrada",
                text="Entrada",
                content=ft.Text("Entrada", color="white"),  # texto branco no dropdown escuro
            ),
            ft.dropdown.Option(
                key="Saída",
                text="Saída",
                content=ft.Text("Saída", color="white"),
            ),
        ],
    )

    # Dropdown de categorias — preenchido dinamicamente com List Comprehension.
    #
    # CONCEITO — List Comprehension:
    #   [ft.dropdown.Option(key=c, text=c, ...) for c in CATEGORIAS]
    #   é equivalente a:
    #     lista = []
    #     for c in CATEGORIAS:
    #         lista.append(ft.dropdown.Option(key=c, text=c, ...))
    #
    # Vantagem: ao adicionar um item em CATEGORIAS (lá no topo do arquivo),
    # ele aparece automaticamente aqui sem tocar neste código.
    campo_categ = ft.Dropdown(
        label="Categoria",
        color="white",
        bgcolor=CAMPO_BG,
        border_color=BORDA,
        focused_border_color="#a09af0",
        label_style=LABEL_COR,
        border_radius=8,
        # Para cada string "c" em CATEGORIAS, cria uma Option com key=c e text=c
        options=[
            ft.dropdown.Option(key=c, text=c, content=ft.Text(c, color="white"))
            for c in CATEGORIAS
        ],
    )

    # Widget de texto para exibir mensagens de erro de validação.
    # Começa vazio ("") — é preenchido dentro de salvar() quando há erro.
    msg_erro = ft.Text("", color="red", size=12)


    # --------------------------------------------------------------------------
    # COMPONENTES DE SAÍDA (OUTPUT WIDGETS)
    # --------------------------------------------------------------------------
    # Criamos referências aos widgets de exibição para poder atualizar
    # seus valores (.value, .color) dentro de atualizar_tela().
    # --------------------------------------------------------------------------

    # Textos do painel de resumo financeiro
    # weight=ft.FontWeight.BOLD → texto em negrito
    txt_entradas = ft.Text("R$ 0,00", size=18, weight=ft.FontWeight.BOLD, color="#00d9a3")  # verde
    txt_saidas   = ft.Text("R$ 0,00", size=18, weight=ft.FontWeight.BOLD, color="#ff4d6d")  # vermelho
    txt_saldo    = ft.Text("R$ 0,00", size=22, weight=ft.FontWeight.BOLD, color="white")

    # ft.Column com scroll interno: a lista de transações tem altura fixa (250px)
    # e rola internamente, independentemente da rolagem da página principal.
    # scroll=ft.ScrollMode.AUTO ativa a barra de rolagem quando necessário.
    lista_tx = ft.Column(scroll=ft.ScrollMode.AUTO, height=250)

    # Column vazia que receberá as barras do gráfico em atualizar_tela()
    grafico = ft.Column()


    # --------------------------------------------------------------------------
    # FUNÇÃO: atualizar_tela()
    # --------------------------------------------------------------------------
    # Implementa o padrão de "reatividade manual" do Flet.
    #
    # Em frameworks modernos (React, Vue, Flutter), a UI atualiza automaticamente
    # quando os dados mudam. No Flet, devemos reconstruir manualmente os widgets
    # e chamar page.update() para enviar as mudanças à tela.
    #
    # Estratégia: LIMPAR e REPOPULAR
    #   1. Limpa a lista de controles: lista_tx.controls.clear()
    #   2. Adiciona novos controles baseados nos dados atuais: .append(widget)
    #   3. Envia as mudanças: page.update()
    # --------------------------------------------------------------------------
    def atualizar_tela():

        # Desempacota o retorno de calcular_saldo() em três variáveis de uma vez
        entradas, saidas, saldo = calcular_saldo()

        # --- Bloco 1: Atualiza os textos do painel de resumo ---

        # .value = atribui novo conteúdo textual ao widget Text
        txt_entradas.value = formatar(entradas)
        txt_saidas.value   = formatar(saidas)
        txt_saldo.value    = formatar(saldo)

        # Operador ternário: muda a COR do saldo conforme o valor
        # saldo >= 0 → verde (#00d9a3) | saldo < 0 → vermelho (#ff4d6d)
        txt_saldo.color = "#00d9a3" if saldo >= 0 else "#ff4d6d"

        # --- Bloco 2: Reconstrói a lista de transações ---

        # .clear() remove todos os widgets filhos da Column
        # É o passo "limpar" antes de "repopular"
        lista_tx.controls.clear()

        # reversed(): itera a lista de trás para frente — mostra as mais recentes primeiro
        # Não modifica a lista original; retorna um iterador reverso temporário
        for t in reversed(transacoes):

            # Define cor e sinal visual conforme o tipo da transação
            cor   = "#00d9a3" if t["tipo"] == "Entrada" else "#ff4d6d"
            sinal = "+" if t["tipo"] == "Entrada" else "-"

            # Cria uma Row (linha horizontal) para cada transação e a adiciona à Column
            lista_tx.controls.append(
                ft.Row([
                    # expand=True faz o texto de descrição ocupar todo o espaço disponível,
                    # "empurrando" os outros elementos para as extremidades da Row
                    ft.Text(t["desc"],  color="white",   size=13, expand=True),
                    ft.Text(t["categ"], color="#aaaaaa", size=12),              # categoria em cinza
                    ft.Text(
                        f"{sinal} {formatar(t['valor'])}",                     # ex: "+ R$ 35,50"
                        color=cor, size=13, weight=ft.FontWeight.BOLD,
                    ),
                ])
            )

        # --- Bloco 3: Reconstrói o gráfico de barras por categoria ---

        grafico.controls.clear()

        # Dicionário acumulador: soma os valores de cada categoria
        # Chave = nome da categoria | Valor = total acumulado
        totais = {}
        for t in transacoes:
            # .get(chave, padrão): retorna o valor atual ou 0 se a chave não existir
            # Equivalente a: totais[categ] = totais[categ] + valor (sem KeyError)
            totais[t["categ"]] = totais.get(t["categ"], 0) + t["valor"]

        # max() com default=1: retorna o maior valor do dicionário
        # default=1 evita ZeroDivisionError quando totais está vazio
        maximo = max(totais.values(), default=1)

        # sorted() com key=lambda: ordena o dicionário por valor (maior primeiro)
        # lambda x: x[1] → acessa o segundo elemento de cada par (chave, valor)
        # reverse=True → ordem decrescente (maior bar primeiro)
        for cat, val in sorted(totais.items(), key=lambda x: x[1], reverse=True):

            # Calcula a proporção desta categoria em relação ao maior valor
            # pct = 1.0 para o maior | pct = 0.5 para metade do maior, etc.
            pct = val / maximo

            grafico.controls.append(
                ft.Column([

                    # Linha com nome da categoria e valor total
                    ft.Row([
                        ft.Text(cat, color="white", size=12, expand=True),
                        ft.Text(formatar(val), color="#aaa", size=12),
                    ]),

                    # Container que representa a barra do gráfico
                    ft.Container(
                        height=12,          # altura fixa da barra em pixels
                        border_radius=6,    # cantos arredondados (cápsula)
                        bgcolor="#6c63ff44", # fundo roxo com opacidade (~27%)
                                            # O "44" no hex é o canal Alpha (transparência)

                        # Row interna com dois Containers: parte preenchida + parte vazia
                        content=ft.Row([

                            # Parte PREENCHIDA: largura proporcional ao valor
                            # int(pct * 100): converte proporção para escala 0–100
                            # expand= no Flet distribui o espaço na proporção dos valores
                            ft.Container(
                                expand=int(pct * 100),  # ex: pct=0.75 → expand=75
                                height=12,
                                bgcolor="#6c63ff",       # roxo sólido
                                border_radius=6,
                            ),

                            # Parte VAZIA: o espaço restante da barra
                            # max(1, ...) garante que expand seja no mínimo 1
                            # (expand=0 causaria erro no Flet)
                            ft.Container(
                                expand=max(1, 100 - int(pct * 100)),  # ex: 100 - 75 = 25
                            ),

                        ], spacing=0),  # spacing=0: as duas partes ficam coladas
                    ),

                ], spacing=4)  # 4px entre a linha de texto e a barra
            )

        # Envia TODAS as alterações acumuladas para a tela de uma só vez.
        # No Flet, page.update() é o "commit" da renderização — sem ele,
        # nenhuma mudança nos widgets fica visível ao usuário.
        page.update()


    # --------------------------------------------------------------------------
    # HANDLER: salvar(e)
    # --------------------------------------------------------------------------
    # Chamado quando o usuário clica no botão "Registrar".
    # Responsável por: validar → criar → limpar campos → atualizar tela.
    #
    # CONCEITO — Tratamento de Erros com try/except:
    #   try:    bloco de código "otimista" (assume que vai funcionar)
    #   except: bloco executado SOMENTE se ocorrer uma exceção no try
    #
    #   ValueError: exceção padrão do Python para valores inválidos/inesperados.
    #   Usamos raise ValueError("msg") para sinalizar erros de validação
    #   e capturamos com except ValueError as ex para exibir a mensagem ao usuário.
    # --------------------------------------------------------------------------
    def salvar(e):

        try:
            # --- Validação 1: campos obrigatórios de texto ---
            # "not campo_desc.value" é True quando value é "" (string vazia)
            if not campo_desc.value or not campo_valor.value:
                raise ValueError("Campos obrigatórios vazios.")

            # --- Conversão e validação do valor monetário ---
            # .replace(",", ".") trata vírgula como separador decimal
            # float() converte a string para número de ponto flutuante
            # Lança ValueError automaticamente se a string não for numérica
            valor = float(campo_valor.value.replace(",", "."))

            # Validação de negócio: valor deve ser positivo
            if valor <= 0:
                raise ValueError("Valor deve ser maior que zero.")

            # --- Validação 2: dropdowns obrigatórios ---
            # Dropdown não selecionado tem .value == None (não string vazia)
            if not campo_tipo.value or not campo_categ.value:
                raise ValueError("Selecione Tipo e Categoria.")

            # --- CREATE: Criação do registro em memória ---
            # Monta um dicionário com todos os dados da transação e appenda na lista global.
            # datetime.now(): retorna data e hora atuais do sistema operacional
            # .strftime("%d/%m/%Y"): formata como "DD/MM/AAAA" (ex: "08/04/2026")
            transacoes.append({
                "desc":  campo_desc.value,
                "valor": valor,
                "tipo":  campo_tipo.value,
                "categ": campo_categ.value,
                "data":  datetime.now().strftime("%d/%m/%Y"),
            })

            # --- Reset dos campos após salvar com sucesso ---
            # Atribuir "" limpa TextFields; None desmarca Dropdowns
            campo_desc.value  = ""
            campo_valor.value = ""
            campo_tipo.value  = None
            campo_categ.value = None
            msg_erro.value    = ""   # limpa qualquer mensagem de erro anterior

            # Redesenha a tela com os dados atualizados (inclui a nova transação)
            atualizar_tela()

        except ValueError as ex:
            # Se qualquer raise ValueError foi disparado, chegamos aqui.
            # str(ex) converte a exceção em string com a mensagem de erro.
            # O "if str(ex) else" é um fallback caso a exceção não tenha mensagem.
            msg_erro.value = str(ex) if str(ex) else "Erro nos dados informados."
            page.update()  # atualiza apenas para mostrar a mensagem de erro


    # --------------------------------------------------------------------------
    # FÁBRICA DE WIDGETS: cartao(titulo, conteudo)
    # --------------------------------------------------------------------------
    # "Fábrica" (Factory) é um padrão de projeto que cria objetos/widgets
    # com configuração padronizada, recebendo apenas os dados variáveis.
    #
    # Aqui, cartao() sempre cria um Container com o mesmo visual (cor, borda,
    # padding, border_radius), variando apenas o título e o conteúdo interno.
    # Isso garante consistência visual em todas as seções do app.
    #
    # Parâmetros:
    #   titulo   → string exibida como rótulo da seção
    #   conteudo → qualquer widget Flet colocado dentro do cartão
    # --------------------------------------------------------------------------
    def cartao(titulo, conteudo):

        return ft.Container(
            content=ft.Column([
                # Título em maiúsculas (convenção visual), cor cinza, tamanho 12px
                ft.Text(titulo, color="#aaaaaa", size=12, weight=ft.FontWeight.BOLD),

                # Espaçador visual de 8px entre o título e o conteúdo
                ft.Container(height=8),

                # Conteúdo variável passado como argumento
                conteudo,
            ]),
            bgcolor="#2a2a3e",                    # fundo azul-escuro médio
            border_radius=14,                     # cantos bem arredondados
            padding=16,                           # espaço interno
            border=ft.border.all(1, "#3a3a5e"),   # borda fina azul-escura
        )


    # --------------------------------------------------------------------------
    # MONTAGEM DO LAYOUT — Árvore de Componentes
    # --------------------------------------------------------------------------
    # page.add() adiciona widgets à página na ordem em que aparecem.
    # O layout segue uma estrutura de ÁRVORE: cada widget pode conter filhos,
    # que por sua vez contêm outros filhos — formando uma hierarquia visual.
    #
    # Estrutura geral:
    #   ├── Cabeçalho (Column centralizada)
    #   ├── Espaçador
    #   ├── ResponsiveRow (3 cartões de resumo)
    #   ├── Espaçador
    #   ├── Cartão de formulário (nova transação)
    #   ├── Espaçador
    #   └── ResponsiveRow (histórico | gráfico)
    # --------------------------------------------------------------------------
    page.add(

        # ── CABEÇALHO ─────────────────────────────────────────────────────────
        # Column com horizontal_alignment=CENTER centraliza os filhos no eixo X.
        # width=float("inf") faz a Column ocupar toda a largura disponível —
        # necessário para que o alinhamento CENTER funcione corretamente.
        ft.Column(
            controls=[
                ft.Text(
                    "💳 Finanças Pessoais",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color="white",
                    text_align=ft.TextAlign.CENTER,  # alinha o texto internamente
                ),
                ft.Text(
                    "Controle suas entradas e saídas",
                    size=13,
                    color="#aaaaaa",
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # centraliza no eixo horizontal
            width=float("inf"),   # largura infinita = ocupa toda a largura da página
        ),

        # Espaçador visual: Container sem conteúdo, apenas com altura definida
        # Usado para criar respiro entre seções (equivalente a margin-bottom no CSS)
        ft.Container(height=16),


        # ── RESUMO FINANCEIRO (3 CARTÕES RESPONSIVOS) ─────────────────────────
        # ResponsiveRow: grade de 12 colunas que se adapta ao tamanho da tela.
        # col={"xs": 12, "sm": 4} significa:
        #   xs (mobile, < ~600px)  → ocupa 12/12 = largura total (empilhados)
        #   sm (desktop, >= ~600px) → ocupa 4/12  = 1/3 da largura (lado a lado)
        #
        # IMPORTANTE: o filho direto de ResponsiveRow deve ter a propriedade "col".
        # Usamos ft.Column([cartao(...)], col={...}) como wrapper para definir col.
        ft.ResponsiveRow([
            ft.Column([cartao("ENTRADAS", txt_entradas)], col={"xs": 12, "sm": 4}),
            ft.Column([cartao("SAÍDAS",   txt_saidas)],   col={"xs": 12, "sm": 4}),
            ft.Column([cartao("SALDO",    txt_saldo)],    col={"xs": 12, "sm": 4}),
        ], spacing=12),  # spacing=12px entre as colunas

        ft.Container(height=16),


        # ── FORMULÁRIO DE NOVA TRANSAÇÃO ──────────────────────────────────────
        # cartao() retorna um Container estilizado que envolve o formulário.
        # O formulário é uma Column com os campos de entrada e o botão.
        cartao("NOVA TRANSAÇÃO", ft.Column([

            campo_desc,              # TextField de descrição

            ft.Container(height=8),  # espaçador entre campos

            campo_valor,             # TextField de valor

            ft.Container(height=8),

            # ResponsiveRow DENTRO do formulário: coloca os dropdowns lado a lado
            # em telas médias/grandes, e empilhados em mobile.
            # col={"xs": 12, "sm": 6} → xs=largura total | sm=metade da largura
            ft.ResponsiveRow([
                ft.Column([campo_tipo],  col={"xs": 12, "sm": 6}),  # dropdown Tipo
                ft.Column([campo_categ], col={"xs": 12, "sm": 6}),  # dropdown Categoria
            ], spacing=8),

            ft.Container(height=8),

            msg_erro,  # texto de erro (inicialmente vazio, preenchido ao falhar)

            # ElevatedButton: botão com fundo preenchido (Material Design)
            # bgcolor = cor de fundo do botão
            # color   = cor do texto/ícone do botão
            # on_click= referência à função handler (sem parênteses!)
            ft.ElevatedButton(
                "Registrar",
                bgcolor="#6c63ff",    # roxo
                color="white",
                on_click=salvar,      # chama salvar(e) ao clicar
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10),  # cantos arredondados
                ),
            ),

        ])),  # fecha ft.Column e cartao()

        ft.Container(height=16),


        # ── SEÇÃO INFERIOR: HISTÓRICO E GRÁFICO ───────────────────────────────
        # ResponsiveRow com dois cartões lado a lado em telas médias/grandes.
        # col={"xs": 12, "md": 6}:
        #   xs (mobile)  → cada cartão ocupa largura total (empilhados)
        #   md (tablet+) → cada cartão ocupa metade da largura (lado a lado)
        # "md" corresponde a telas >= ~900px (médias/grandes).
        ft.ResponsiveRow([
            ft.Column(
                [cartao("HISTÓRICO", lista_tx)],         # lista de transações com scroll
                col={"xs": 12, "md": 6},
            ),
            ft.Column(
                [cartao("GASTOS POR CATEGORIA", grafico)],  # gráfico de barras
                col={"xs": 12, "md": 6},
            ),
        ], spacing=12),

        # Espaçador final: respiro na parte inferior da página
        ft.Container(height=20),

    )  # fecha page.add()


# ==============================================================================
# PONTO DE ENTRADA DO PROGRAMA
# ==============================================================================
# ft.run(main) inicializa o framework Flet, abre a janela do sistema operacional
# e chama main(page) injetando o objeto page automaticamente.
#
# Esta linha sempre deve ser a última do arquivo.
# Nada após ela é executado durante o ciclo de vida normal do app.
# ==============================================================================
ft.run(main)