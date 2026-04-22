# ==============================================================================
# SMARTPANEL — Aplicativo Desktop/Mobile com Python + Flet
# ==============================================================================
# O Flet é uma biblioteca Python que permite criar aplicativos com interface
# gráfica (GUI) para desktop, web e mobile, aproveitando os widgets do Flutter.
#
# Para instalar:
#   pip install flet==0.81
#
# Para executar:
#   python smart_panel_comentado.py
# ==============================================================================


# ------------------------------------------------------------------------------
# IMPORTAÇÃO DA BIBLIOTECA
# ------------------------------------------------------------------------------
# "import flet as ft" carrega a biblioteca Flet e cria o apelido "ft".
# A partir daqui, escrevemos ft.Text() em vez de flet.Text().
# O apelido "ft" é uma convenção da comunidade Flet — assim como "np" para NumPy.
import flet as ft


# ------------------------------------------------------------------------------
# CONSTANTE GLOBAL — BREAKPOINT RESPONSIVO
# ------------------------------------------------------------------------------
# Constantes são variáveis cujos valores não mudam durante a execução.
# Por convenção, constantes em Python são escritas em MAIÚSCULAS.
#
# BREAKPOINT_MOBILE define a largura mínima (em pixels) para layout desktop.
# → Janela com largura < 600px  : layout MOBILE  (barra de navegação inferior)
# → Janela com largura >= 600px : layout DESKTOP (menu lateral)
#
# Centralizar esse valor aqui facilita a manutenção: se precisarmos mudar
# o breakpoint, alteramos só nesta linha, e o efeito se propaga por todo o app.
BREAKPOINT_MOBILE = 600   # unidade: pixels


# ==============================================================================
# FUNÇÃO: paleta(dark)
# ==============================================================================
# Esta função resolve um problema fundamental do Flet: widgets com "bgcolor"
# fixo (ex: bgcolor=ft.Colors.BLUE_50) NÃO mudam automaticamente ao trocar
# o tema — eles ficam sempre com aquela cor, independente do tema ativo.
#
# Solução: centralizar TODAS as cores do app aqui.
# A cada troca de tema, chamamos paleta(True) ou paleta(False), obtemos um
# novo dicionário e reconstruímos toda a interface com as cores corretas.
#
# Tipo dos parâmetros (type hints):
#   dark: bool  → aceita True (escuro) ou False (claro)
#   -> dict     → retorna um dicionário Python
# ==============================================================================
def paleta(dark: bool) -> dict:

    # Bloco executado quando dark=True (tema ESCURO ativo)
    if dark:
        return {

            # ------------------------------------------------------------------
            # SUPERFÍCIES — cores de fundo dos elementos visuais
            # ------------------------------------------------------------------
            # GREY_900 é o cinza mais escuro disponível no Flet (quase preto).
            # Usamos tons de cinza escuro para simular o "Material Dark Theme".
            "bg_page":    ft.Colors.GREY_900,   # fundo da janela inteira
            "bg_sidebar": ft.Colors.GREY_900,   # fundo do menu lateral
            "bg_card":    ft.Colors.GREY_800,   # fundo dos cards genéricos

            # with_opacity(opacidade, cor): aplica transparência à cor.
            # O valor 0.15 significa 15% de opacidade (quase transparente).
            # Isso cria um toque sutil de cor sem "estourar" o fundo escuro.
            # Exemplo: bg_card_blue no dark = azul muito transparente sobre cinza.
            "bg_card_blue":   ft.Colors.with_opacity(0.15, ft.Colors.BLUE_200),
            "bg_card_green":  ft.Colors.with_opacity(0.15, ft.Colors.GREEN_200),
            "bg_card_orange": ft.Colors.with_opacity(0.15, ft.Colors.ORANGE_200),
            "bg_dica":        ft.Colors.with_opacity(0.15, ft.Colors.AMBER_200),
            "bg_info_box":    ft.Colors.with_opacity(0.12, ft.Colors.BLUE_200),
            "bg_menu_ativo":  ft.Colors.with_opacity(0.18, ft.Colors.BLUE_200),

            # ------------------------------------------------------------------
            # BORDAS — linhas ao redor dos containers e cards
            # ------------------------------------------------------------------
            # No tema escuro, bordas mais escuras evitam contraste excessivo.
            "borda_padrao":     ft.Colors.GREY_700,
            "borda_blue":       ft.Colors.BLUE_800,
            "borda_green":      ft.Colors.GREEN_800,
            "borda_orange":     ft.Colors.ORANGE_800,
            "borda_dica":       ft.Colors.AMBER_700,
            "borda_info":       ft.Colors.BLUE_800,
            "borda_menu_ativo": ft.Colors.BLUE_700,
            "borda_sidebar":    ft.Colors.GREY_700,

            # ------------------------------------------------------------------
            # TEXTOS — cores dos textos em cada contexto
            # ------------------------------------------------------------------
            # No tema escuro, textos devem ser CLAROS para contrastar com o fundo.
            "txt_titulo":     ft.Colors.WHITE,      # títulos principais de cada página
            "txt_subtitulo":  ft.Colors.GREY_400,   # textos de apoio/descrição
            "txt_card_label": ft.Colors.GREY_400,   # rótulo no topo de cada card
            "txt_card_valor": ft.Colors.WHITE,      # valor/conteúdo dentro do card
            "txt_menu_ativo": ft.Colors.BLUE_300,   # item selecionado no menu
            "txt_menu_normal":ft.Colors.GREY_300,   # itens não selecionados no menu
            "txt_dica":       ft.Colors.AMBER_200,  # texto das caixas de dica (amarelas)
            "txt_semana":     ft.Colors.GREY_600,   # texto de rodapé/versão do app
            "txt_divider":    ft.Colors.GREY_700,   # cor das linhas divisórias (Divider)

            # ------------------------------------------------------------------
            # ÍCONES — cores dos ícones no menu lateral
            # ------------------------------------------------------------------
            "icone_menu_ativo": ft.Colors.BLUE_300,  # ícone do item ativo
            "icone_menu_norm":  ft.Colors.GREY_400,  # ícone dos itens inativos

            # ------------------------------------------------------------------
            # AVATAR — círculo com a inicial do nome do usuário
            # ------------------------------------------------------------------
            "avatar_bg": ft.Colors.BLUE_900,   # cor de fundo do círculo
            "avatar_fg": ft.Colors.BLUE_200,   # cor da letra dentro do círculo

            # ------------------------------------------------------------------
            # SOMBRA — efeito de profundidade/elevação nos cards
            # ------------------------------------------------------------------
            # 30% de opacidade no escuro cria sombra visível sem exagero.
            "sombra": ft.Colors.with_opacity(0.30, ft.Colors.BLACK),
        }

    # Bloco executado quando dark=False (tema CLARO ativo)
    else:
        return {

            # Superfícies claras — branco e cinza bem claro (GREY_50)
            "bg_page":        ft.Colors.WHITE,
            "bg_sidebar":     ft.Colors.GREY_50,
            "bg_card":        ft.Colors.WHITE,
            "bg_card_blue":   ft.Colors.BLUE_50,     # azul pastel
            "bg_card_green":  ft.Colors.GREEN_50,    # verde pastel
            "bg_card_orange": ft.Colors.ORANGE_50,   # laranja pastel
            "bg_dica":        ft.Colors.AMBER_50,    # âmbar pastel
            "bg_info_box":    ft.Colors.BLUE_50,
            "bg_menu_ativo":  ft.Colors.BLUE_50,

            # Bordas suaves — tons médios de cada cor
            "borda_padrao":     ft.Colors.BLUE_200,
            "borda_blue":       ft.Colors.BLUE_200,
            "borda_green":      ft.Colors.GREEN_200,
            "borda_orange":     ft.Colors.ORANGE_200,
            "borda_dica":       ft.Colors.AMBER_200,
            "borda_info":       ft.Colors.BLUE_100,
            "borda_menu_ativo": ft.Colors.BLUE_200,
            "borda_sidebar":    ft.Colors.GREY_200,

            # Textos escuros — legíveis sobre fundo claro
            "txt_titulo":     ft.Colors.BLACK,
            "txt_subtitulo":  ft.Colors.GREY_600,
            "txt_card_label": ft.Colors.GREY_600,
            "txt_card_valor": ft.Colors.BLACK,
            "txt_menu_ativo": ft.Colors.BLUE_700,
            "txt_menu_normal":ft.Colors.GREY_700,
            "txt_dica":       ft.Colors.AMBER_900,
            "txt_semana":     ft.Colors.GREY_400,
            "txt_divider":    ft.Colors.GREY_200,

            # Ícones
            "icone_menu_ativo": ft.Colors.BLUE_700,
            "icone_menu_norm":  ft.Colors.GREY_500,

            # Avatar
            "avatar_bg": ft.Colors.BLUE_100,
            "avatar_fg": ft.Colors.BLUE_700,

            # Sombra discreta — 7% de opacidade no claro é suficiente
            "sombra": ft.Colors.with_opacity(0.07, ft.Colors.BLACK),
        }
        
def criar_card(titulo: string, conteudo: ft.Control, p: dict, cor_borda_key: str = "borda_padrao")->ft.Container:
    
    return ft.Container(
        content=ft.Column([
            ft.Text(titulo, size=13, weight="bold", color=p["txt_card_label"]),
            conteudo,
        ],
            spacing=10,
            tight=True,
        ),
        padding=16,
        bgcolor=p["bg_card"],
        border=ft.border.all(1, p[cor_borda_key]),
        border_radius=12,
        shadow=ft.BoxShadow(blur_radius=8, spread_radius=0, color=p["sombra"], offset=ft.Offset(0,2)),
    )        

def criar_botao_primario(texto, icone, on_click, expend=False):
    
    return ft.ElevatedButton(
        content=ft.Row(
            [
                ft.Icon(icone, size=16),
                ft.Text(texto, size=14),
            ],
            spacing=6,
            tight=True,
        ),
        #ver esse onclick e expand
        on_click=on_click,
        expand=expand,
        
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8)
        )
    )
    
def criar_botao_secundario(texto, icone, on_click, expand=False):
    return ft.ElevatedButton(
        content=ft.Row(
            [
                ft.Icon(icone, size=16),
                ft.Text(texto, size=14),
            ],
            spacing=6,
            tight=True,
        ),
        #ver esse onclick e expand
        on_click=on_click,
        expand=expand,
        
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8)
        )
    )
        
def criar_dica(mensagem: str, p:dict)->ft.Container:
    
    return ft.Container(
        content=ft.Row([
            ft.Icon(ft.Icons.LIGHTBULB_OUTLINED, color=ft.Colors.AMBER_700, size=16),
            ft.Text(mensagem, size=13, color=p["txt_dica"], expand=True)
        ],
        spacing=8,
        ),
        padding=ft.Padding(12,10,12,10),
        bgcolor=p["bg_dica"],
        border=ft.border.all(1, p["borda_dica"]),        
    )



ft.run(main)