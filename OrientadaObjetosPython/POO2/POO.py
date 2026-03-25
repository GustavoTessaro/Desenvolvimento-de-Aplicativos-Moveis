# =============================================================================
# PROJETO: Zoológico Virtual - Pilares da Programação Orientada a Objetos (POO)
# BIBLIOTECA: Flet (https://flet.dev) - cria apps desktop, web e mobile em Python
# OBJETIVO DIDÁTICO: Demonstrar os 4 pilares da POO com interface responsiva
#
# OS 4 PILARES DEMONSTRADOS NESTE CÓDIGO:
#   1. ABSTRAÇÃO    - Classe Animal (define o "contrato" sem implementar tudo)
#   2. HERANÇA      - Leao e Elefante herdam de Animal
#   3. ENCAPSULAMENTO - Atributo privado __nome + método getter get_nome()
#   4. POLIMORFISMO - Mesmo método emitir_som() com comportamentos diferentes
# =============================================================================

import flet as ft
# 'flet' é o framework que usaremos para criar a interface gráfica.
# Com ele podemos criar apps visuais usando apenas Python.

from abc import ABC, abstractmethod
# 'ABC' (Abstract Base Class) permite criar classes abstratas.
# 'abstractmethod' é um decorador que marca métodos que OBRIGAM a implementação.

# =============================================================================
# PILAR 1: ABSTRAÇÃO
# =============================================================================
# Uma classe abstrata é como um CONTRATO ou MOLDE.
# Ela define O QUÊ as subclasses devem fazer, mas NÃO COMO devem fazer.
# Não é possível instanciar Animal() diretamente — ela existe apenas como base.
# =============================================================================
class Animal(ABC):
    # 'ABC' indica que esta é uma Classe Base Abstrata (não pode ser instanciada)

    def __init__(self, nome):
        # Construtor: executado automaticamente ao criar um objeto desta classe.
        # Recebe 'nome' como parâmetro para identificar o animal.

        # =====================================================================
        # PILAR 3: ENCAPSULAMENTO
        # =====================================================================
        # O prefixo '__' (duplo underline) torna o atributo PRIVADO.
        # Isso significa que '__nome' só pode ser acessado DENTRO desta classe.
        # Tentativas de acesso externo (ex: animal.__nome) gerarão erro.
        # Isso protege o dado e força o uso dos métodos getter/setter.
        # =====================================================================
        self.__nome = nome
        # '__nome' é o atributo privado. Apenas os métodos desta classe podem lê-lo.

    def get_nome(self):
        # GETTER: método público que permite leitura CONTROLADA do atributo privado.
        # É a forma "oficial" e segura de obter o nome fora da classe.
        # Boa prática: nunca expor atributos privados diretamente.
        return self.__nome
        # Retorna o valor de __nome de forma segura e controlada.

    @abstractmethod
    def emitir_som(self):
        # MÉTODO ABSTRATO: define uma obrigação para todas as subclasses.
        # Qualquer classe que herdar de Animal PRECISA implementar este método.
        # Se não implementar, Python lançará um TypeError ao tentar instanciar.
        # O 'pass' indica que não há implementação aqui — só a assinatura do método.
        pass

    @abstractmethod
    def get_especie(self):
        # Outro método abstrato: força subclasses a informarem sua espécie.
        # Cada animal concreto (Leao, Elefante) saberá responder qual é sua espécie.
        pass


# =============================================================================
# PILAR 2: HERANÇA
# =============================================================================
# 'Leao' herda de 'Animal': recebe todos os atributos e métodos da classe pai.
# Ao herdar, Leao TAMBÉM É UM Animal — essa é a relação "é-um" da herança.
# A herança evita repetição de código (princípio DRY: Don't Repeat Yourself).
# =============================================================================
class Leao(Animal):
    # Leao é uma subclasse (filha) de Animal.
    # Ela herda: __nome, get_nome(), e a obrigação de implementar os abstratos.

    def __init__(self, nome):
        # Construtor da subclasse. Recebe o nome e repassa para o pai.
        super().__init__(nome)
        # 'super()' acessa a classe pai (Animal).
        # '__init__(nome)' chama o construtor do pai para inicializar '__nome'.
        # Sem isso, o atributo privado não seria criado corretamente.

    def get_especie(self):
        # Implementação concreta do método abstrato get_especie().
        # Aqui dizemos explicitamente que este animal é um "Leão".
        return "Leão"

    # =========================================================================
    # PILAR 4: POLIMORFISMO
    # =========================================================================
    # 'Poli' = muitas | 'morphos' = formas.
    # O MESMO método 'emitir_som' tem comportamentos DIFERENTES em cada subclasse.
    # Leao implementa emitir_som() à sua maneira — com rugido.
    # =========================================================================
    def emitir_som(self):
        # Implementação concreta do método abstrato emitir_som() para o Leão.
        return "ROAAARRR! 🦁"
        # O polimorfismo permite que chamemos animal.emitir_som() sem saber
        # se é um Leao ou Elefante — o Python resolve isso em tempo de execução.


# =============================================================================
# PILAR 2: HERANÇA (segunda subclasse)
# =============================================================================
class Elefante(Animal):
    # Elefante também é uma subclasse de Animal.
    # Mesma estrutura do Leao, mas com implementações próprias.

    def __init__(self, nome):
        # Construtor: repassa o nome para o construtor da classe pai.
        super().__init__(nome)
        # Novamente usamos super() para garantir a inicialização correta do __nome.

    def get_especie(self):
        # Implementação concreta: este animal se identifica como "Elefante".
        return "Elefante"

    def emitir_som(self):
        # POLIMORFISMO em ação: mesmo nome de método, comportamento totalmente diferente.
        # O som do elefante é completamente distinto do som do leão.
        return "PAAACHUUUM! 🐘"
        # Em tempo de execução, Python decide qual emitir_som() chamar
        # baseado no TIPO REAL do objeto (Leao ou Elefante).


# =============================================================================
# INTERFACE FLET — RESPONSIVA
# =============================================================================
# A função 'main' é o ponto de entrada do aplicativo Flet.
# 'page' representa a janela/tela do app e dá acesso a todas as configurações visuais.
# =============================================================================
def main(page: ft.Page):

    # --- CONFIGURAÇÕES GERAIS DA JANELA ---

    page.title = "Zoológico Virtual OOP"
    # Define o título exibido na barra superior da janela do sistema operacional.

    page.theme_mode = ft.ThemeMode.DARK
    # Define o tema: DARK (escuro) ou LIGHT (claro).
    # O tema escuro é mais confortável para longas sessões de uso.

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # Alinha todos os filhos da página ao centro no eixo horizontal.

    page.scroll = ft.ScrollMode.AUTO
    # Habilita rolagem automática quando o conteúdo ultrapassa o tamanho da tela.
    # Essencial para responsividade em telas pequenas.

    page.padding = ft.padding.symmetric(horizontal=16, vertical=24)
    # Define margens internas da página: 16px nas laterais, 24px em cima e embaixo.
    # Evita que o conteúdo "grude" nas bordas da tela — boa prática de layout.

    page.bgcolor = "#1a1a2e"
    # Define a cor de fundo da página em hexadecimal.
    # Usamos um azul-escuro profundo para dar identidade visual ao app.

    # --- RESPONSIVIDADE: captura mudanças de tamanho da janela ---

    def on_resize(e):
        # Esta função é chamada AUTOMATICAMENTE sempre que a janela é redimensionada.
        # 'e' contém informações do evento, incluindo as novas dimensões da tela.
        atualizar_layout()
        # Chamamos nossa função de layout para reposicionar os elementos.

    page.on_resized = on_resize
    # Registra 'on_resize' como o handler (tratador) do evento de redimensionamento.
    # Sempre que o usuário arrastar a borda da janela, on_resize será chamado.

    # --- COMPONENTES VISUAIS (WIDGETS) ---
    # Cada widget abaixo é um elemento da interface que será exibido ao usuário.

    txt_titulo = ft.Text(
        "🦁 Zoológico Virtual",
        # Texto exibido — inclui emoji para tornar mais visual e atraente.
        size=28,
        # Tamanho da fonte em pixels.
        weight=ft.FontWeight.BOLD,
        # Deixa o texto em negrito para destacar o título.
        color="#f0a500",
        # Cor dourada que remete à savana africana — escolha temática consciente.
        text_align=ft.TextAlign.CENTER,
        # Centraliza o texto dentro do seu espaço disponível.
    )

    txt_subtitulo = ft.Text(
        "Demonstração dos 4 Pilares da POO",
        # Subtítulo explicativo para contextualizar o propósito didático do app.
        size=13,
        # Fonte menor para hierarquia visual (título > subtítulo).
        color="#aaaacc",
        # Cor acinzentada suave, menos destaque que o título.
        text_align=ft.TextAlign.CENTER,
        italic=True,
        # Itálico reforça visualmente que é um subtítulo/descrição.
    )

    input_nome = ft.TextField(
        label="Nome do Animal",
        # Rótulo flutuante que aparece acima do campo quando ele tem foco.
        hint_text="Ex: Simba, Dumbo...",
        # Texto de dica que aparece dentro do campo quando está vazio.
        border_radius=12,
        # Arredonda os cantos do campo — estética moderna e amigável.
        border_color="#f0a500",
        # Cor da borda: dourado para manter consistência com o tema.
        focused_border_color="#ffffff",
        # Cor da borda quando o campo está com foco (cursor ativo): branco.
        label_style=ft.TextStyle(color="#aaaacc"),
        # Estilo do rótulo: cor acinzentada para não competir com o conteúdo.
        cursor_color="#f0a500",
        # Cor do cursor de texto: dourado, seguindo o tema.
    )

    radio_especie = ft.RadioGroup(
        # RadioGroup agrupa os botões de rádio para que apenas um possa ser selecionado.
        content=ft.Container(
            # Container envolve a Row para forçar centralização no browser e desktop.
            # CORREÇÃO: usar Container com alignment garante centralização correta
            # no modo web, onde ft.Row sozinha pode perder o alinhamento central.
            content=ft.Row(
                # Row organiza os filhos em uma linha horizontal.
                [
                    ft.Radio(
                        value="leao",
                        # Valor interno que identifica esta opção no código.
                        label="Leão 🦁",
                        # Texto visível ao usuário ao lado do botão.
                        fill_color="#f0a500",
                        # Cor de preenchimento do radio quando selecionado.
                    ),
                    ft.Radio(
                        value="elefante",
                        # Valor interno para a opção do elefante.
                        label="Elefante 🐘",
                        fill_color="#f0a500",
                        # Mesma cor dourada para consistência visual.
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                # Centraliza os radios dentro da Row.
            ),
            alignment=ft.Alignment(0, 0),
            # Garante que o Container também alinhe seu conteúdo ao centro.
            # CORREÇÃO: ft.Alignment(x, y) onde x=0 e y=0 significa centro exato.
            # Valores vão de -1 (esquerda/topo) até 1 (direita/baixo).
        )
    )

    lbl_resultado = ft.Text(
        # Campo de texto que exibirá o resultado após o clique no botão.
        size=20,
        # Tamanho de fonte médio — destaque sem exagero.
        weight=ft.FontWeight.BOLD,
        # Negrito para dar peso visual ao resultado.
        color="#ffffff",
        # Branco puro para máximo contraste sobre o fundo escuro.
        text_align=ft.TextAlign.CENTER,
        # Centralizado para ficar bem posicionado na tela.
    )

    # Container que envolve o resultado com estilo visual de "card"
    card_resultado = ft.Container(
        content=lbl_resultado,
        # O conteúdo do card é o texto de resultado.
        padding=ft.padding.all(20),
        # Espaçamento interno de 20px em todos os lados — "respiro" visual.
        border_radius=16,
        # Bordas bem arredondadas para estética de card moderno.
        bgcolor="#252540",
        # Cor de fundo levemente diferente do fundo da página para criar contraste.
        border=ft.border.all(1, "#f0a500"),
        # Borda fina dourada que define o card visualmente.
        visible=False,
        # Inicialmente invisível. Só aparecerá após o clique no botão.
        animate_opacity=300,
        # Animação de 300ms ao mudar a opacidade — transição suave de aparecimento.
    )

    # Indicador de carregamento/feedback visual ao clicar
    icone_animal = ft.Text(
        "",
        # Começa vazio; será preenchido com o emoji do animal escolhido.
        size=64,
        # Tamanho grande para dar impacto visual ao emoji.
        text_align=ft.TextAlign.CENTER,
        animate_scale=ft.Animation(400, ft.AnimationCurve.BOUNCE_OUT),
        # Animação de escala com 400ms e curva "bounce" (efeito de quique).
        # CORREÇÃO: 'ft.Animation' (direto) — 'ft.animation.Animation' foi descontinuado.
        # Dá vida ao emoji quando ele aparece na tela.
    )

    # --- FUNÇÃO PRINCIPAL: lógica do botão ---

    def interagir_com_animal(e):
        # Esta função é chamada quando o usuário clica em "Ouvir Animal".
        # 'e' é o objeto do evento de clique (não usamos aqui, mas é obrigatório).

        nome_digitado = input_nome.value
        # Lê o texto que o usuário digitou no campo input_nome.
        # '.value' acessa o conteúdo atual do TextField.

        especie_selecionada = radio_especie.value
        # Lê qual Radio foi selecionado: "leao" ou "elefante".
        # Se nenhum foi selecionado, o valor será None.

        # --- VALIDAÇÃO DE ENTRADA ---
        if not nome_digitado or not especie_selecionada:
            # 'not nome_digitado' é True se o campo está vazio ou só tem espaços.
            # 'not especie_selecionada' é True se nenhum radio foi marcado.
            # O 'or' significa: se QUALQUER UMA das condições for verdadeira, exibe erro.
            lbl_resultado.value = "⚠️ Por favor, preencha o nome\ne selecione uma espécie!"
            # Define a mensagem de erro no texto de resultado.
            lbl_resultado.color = "#ff6b6b"
            # Vermelho suave para indicar erro — convenção universal de UI.
            card_resultado.visible = True
            # Torna o card visível para mostrar a mensagem de erro.
            icone_animal.value = "❓"
            # Exibe um ponto de interrogação como feedback visual de erro.
            icone_animal.scale = 1
            # Reseta a escala para disparar a animação novamente.
            page.update()
            # OBRIGATÓRIO: atualiza a tela para refletir todas as mudanças acima.
            return
            # Interrompe a função aqui — não executa o código abaixo.

        # --- INSTANCIAÇÃO POLIMÓRFICA ---
        # A variável 'animal_objeto' recebe o tipo Animal (genérico).
        # Dependendo da escolha, ela receberá um Leao ou um Elefante.
        # Isso é polimorfismo: o mesmo tipo de variável comporta objetos diferentes.

        animal_objeto = None
        # Inicializamos como None; será sobrescrito abaixo.

        if especie_selecionada == "leao":
            # Se o usuário selecionou "leao"...
            animal_objeto = Leao(nome_digitado)
            # ...instanciamos a classe Leao passando o nome digitado.
            # O construtor de Leao chama super().__init__(nome) que guarda em __nome.
            emoji = "🦁"
            # Emoji correspondente ao leão para exibir no ícone animado.

        elif especie_selecionada == "elefante":
            # Se o usuário selecionou "elefante"...
            animal_objeto = Elefante(nome_digitado)
            # ...instanciamos a classe Elefante.
            emoji = "🐘"
            # Emoji correspondente ao elefante.

        # =====================================================================
        # POLIMORFISMO NA PRÁTICA:
        # A partir daqui, o código NÃO PRECISA SABER se é Leao ou Elefante.
        # Chamamos os mesmos métodos em ambos — o Python resolve na execução.
        # Isso é o poder do polimorfismo: código genérico que funciona com qualquer
        # subclasse de Animal, presente ou futura (Tigre, Girafa, etc.).
        # =====================================================================

        nome_real = animal_objeto.get_nome()
        # Usa o GETTER (Encapsulamento) para acessar o atributo privado __nome.
        # Não acessamos animal_objeto.__nome diretamente — respeitamos o encapsulamento.

        especie_real = animal_objeto.get_especie()
        # Chama get_especie() — método abstrato implementado por Leao ou Elefante.
        # Python decide em tempo de execução qual versão do método usar.

        som = animal_objeto.emitir_som()
        # POLIMORFISMO: mesma chamada, resultado diferente.
        # Se for Leao: retorna "ROAAARRR! 🦁"
        # Se for Elefante: retorna "PAAACHUUUM! 🐘"

        # --- ATUALIZAÇÃO DA INTERFACE ---

        icone_animal.value = emoji
        # Atualiza o texto do ícone com o emoji do animal correspondente.
        icone_animal.scale = 0
        # Reseta a escala para 0 (invisível) para disparar a animação de bounce.
        page.update()
        # Atualiza a tela com scale=0 para criar o "antes" da animação.

        icone_animal.scale = 1
        # Volta a escala para 1 (tamanho normal), disparando a animação bounce.

        lbl_resultado.value = f"Eu sou {nome_real}, o {especie_real}!\n\n{som}"
        # Formata a mensagem final com os dados obtidos via polimorfismo.
        # Usamos f-string para interpolação de variáveis dentro da string.

        lbl_resultado.color = "#f0a500"
        # Muda a cor do texto para dourado ao exibir um resultado de sucesso.

        card_resultado.visible = True
        # Torna o card visível (com animação suave de opacidade de 300ms).

        input_nome.value = ""
        # Limpa o campo de nome para facilitar a próxima interação.

        page.update()
        # OBRIGATÓRIO: aplica todas as mudanças visuais definidas acima na tela.

    # --- BOTÃO PRINCIPAL ---

    btn_ouvir = ft.ElevatedButton(
        "Ouvir Animal",
        # Texto exibido dentro do botão.
        icon=ft.Icons.VOLUME_UP,
        # Ícone de volume ao lado do texto — reforça a ação de "ouvir".
        # ATENÇÃO: 'ft.Icons' (I maiúsculo) é obrigatório nas versões recentes do Flet.
        on_click=interagir_com_animal,
        # Define a função chamada quando o botão for clicado.
        style=ft.ButtonStyle(
            color="#1a1a2e",
            # Cor do texto e ícone do botão: azul-escuro (contrasta com o fundo dourado).
            bgcolor="#f0a500",
            # Cor de fundo do botão: dourado — destaca o botão principal da tela.
            shape=ft.RoundedRectangleBorder(radius=12),
            # Define a forma do botão com bordas arredondadas de 12px.
            padding=ft.padding.symmetric(horizontal=32, vertical=14),
            # Espaçamento interno: mais largo que alto — botão mais "robusto" visualmente.
        ),
    )

    # --- RODAPÉ DIDÁTICO ---

    txt_pilares = ft.Text(
        "🔷 Abstração  🔶 Herança  🔹 Encapsulamento  🔸 Polimorfismo",
        # Lembrete visual dos 4 pilares da POO para os alunos.
        size=11,
        # Fonte pequena — informação de apoio, não destaque principal.
        color="#666688",
        # Cor discreta para não distrair do conteúdo principal.
        text_align=ft.TextAlign.CENTER,
        # Centralizado para ficar bem no rodapé.
    )

    # =========================================================================
    # LAYOUT RESPONSIVO
    # =========================================================================
    # A função abaixo reconstrói o layout sempre que a janela muda de tamanho.
    # Em telas largas: layout mais espaçado.
    # Em telas estreitas (mobile/tablet): layout mais compacto.
    # =========================================================================

    def atualizar_layout():
        largura = page.width or 400
        # Obtém a largura atual da janela.
        # 'or 400' define um valor padrão caso page.width seja None na inicialização.

        # Define largura máxima do conteúdo de forma responsiva:
        if largura < 400:
            # Telas muito pequenas (smartphones compactos):
            largura_conteudo = largura - 16
            # Usa quase toda a largura disponível com pequena margem.
        elif largura < 700:
            # Telas médias (smartphones grandes, tablets menores):
            largura_conteudo = largura - 32
            # Margem um pouco maior nas laterais.
        else:
            # Telas grandes (tablets, desktops):
            largura_conteudo = min(largura - 48, 520)
            # Limita a 520px para não esticar demais em monitores largos.
            # 'min()' garante que nunca ultrapasse 520px.

        input_nome.width = largura_conteudo
        # Ajusta a largura do campo de nome conforme o tamanho da tela.

        card_resultado.width = largura_conteudo
        # Ajusta o card de resultado à mesma largura do campo de entrada.

        page.update()
        # Aplica as mudanças de layout na tela.

    # --- MONTAGEM DA PÁGINA ---
    # Aqui organizamos todos os widgets em uma estrutura de coluna vertical.
    # A ordem aqui define a ordem de exibição na tela (de cima para baixo).

    page.add(
        # Adiciona um único filho à página: uma Column centralizada.
        ft.Column(
            [
                # --- CABEÇALHO ---
                ft.Container(height=10),
                # Espaçador invisível de 10px acima do título.

                txt_titulo,
                # Título principal "🦁 Zoológico Virtual".

                txt_subtitulo,
                # Subtítulo "Demonstração dos 4 Pilares da POO".

                ft.Container(height=16),
                # Espaçador de 16px entre cabeçalho e formulário.

                ft.Divider(color="#333355", thickness=1),
                # Linha separadora horizontal discreta para organizar visualmente.

                ft.Container(height=16),
                # Espaçador após o divisor.

                # --- FORMULÁRIO ---
                ft.Text("Nome do animal:", size=14, color="#aaaacc"),
                # Rótulo acima do campo de texto — orienta o usuário.

                input_nome,
                # Campo de texto onde o usuário digita o nome do animal.

                ft.Container(height=12),
                # Pequeno espaçador entre o campo e os radios.

                ft.Text("Selecione a espécie:", size=14, color="#aaaacc"),
                # Rótulo acima dos radio buttons.

                radio_especie,
                # Grupo de opções de espécie (Leão ou Elefante).

                ft.Container(height=20),
                # Espaçador antes do botão.

                btn_ouvir,
                # Botão principal "Ouvir Animal".

                ft.Container(height=24),
                # Espaçador após o botão, antes do resultado.

                # --- RESULTADO ---
                icone_animal,
                # Emoji grande e animado do animal escolhido.

                card_resultado,
                # Card com o texto do resultado (som do animal).

                ft.Container(height=24),
                # Espaçador antes do rodapé.

                ft.Divider(color="#333355", thickness=1),
                # Segundo divisor antes do rodapé.

                ft.Container(height=8),
                # Pequeno espaçador antes do texto dos pilares.

                txt_pilares,
                # Rodapé com os 4 pilares da POO listados.

                ft.Container(height=16),
                # Espaçador final para não ficar colado na borda inferior.
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            # Centraliza todos os filhos da Column no eixo horizontal.
            spacing=0,
            # Espaçamento entre filhos = 0 (usamos Containers como espaçadores
            # para controle mais preciso do espaçamento individual).
        )
    )

    atualizar_layout()
    # Chama o layout responsivo assim que o app inicia, para configurar os tamanhos iniciais.


# =============================================================================
# PONTO DE ENTRADA DO APLICATIVO
# =============================================================================
ft.app(main)
# 'ft.app()' inicializa o aplicativo Flet e chama a função 'main' passando
# um objeto 'page' que representa a janela do app.
# ATENÇÃO: use 'ft.app()' — o antigo 'ft.run()' foi descontinuado.
# =============================================================================