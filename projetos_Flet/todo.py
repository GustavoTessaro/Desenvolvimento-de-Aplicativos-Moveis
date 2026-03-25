# Bloco 01
import flet as ft  # Importa o módulo flet criando o alias 'ft' — todos os componentes serão acessados como ft.NomeDoComponente

# Bloco 02
def main(page: ft.Page):  # Define a função principal; o parâmetro 'page' é injetado pelo ft.run() e representa a janela do app
    page.title = "Mini To-Do App"  # Define o texto exibido na aba do navegador (ou barra de título na janela nativa)
    page.theme_mode = ft.ThemeMode.LIGHT  # Força o tema claro (Material Design Light) independentemente da preferência do sistema operacional
    page.padding = 20  # 20px de espaçamento interno em todos os lados da página — evita que controles grudem nas bordas
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Centraliza todos os filhos diretos da page no eixo horizontal (CrossAxis = perpendicular ao fluxo)
    page.scroll = ft.ScrollMode.AUTO  # Habilita barra de rolagem automática: aparece apenas quando o conteúdo exceder a altura disponível

    # Bloco 03
    tasks = []  # Lista Python que guarda referências a cada Container de tarefa — serve como estado local da aplicação
    task_input = ft.TextField(  # Cria o campo de texto para entrada da nova tarefa — ainda não adicionado à página neste ponto
        label="Digite uma tarefa",  # Rótulo flutuante que sobe quando o campo recebe foco (comportamento padrão do Material Design)
        expand=True,  # O campo expandirá para ocupar todo o espaço disponível no Row, deixando apenas o botão à direita
        on_submit=lambda e: add_task(e)  # Registra callback para o evento de submissão (tecla Enter) — chama add_task() ao pressionar Enter
    )
    task_list = ft.ListView(  # ListView renderiza listas longas com virtualização (só renderiza itens visíveis) — mais eficiente que Column
        expand=True,  # Expande para ocupar todo o espaço vertical disponível dentro do Column pai
        spacing=10,  # 10px de espaçamento vertical entre cada item da lista — substitui margins individuais nos itens
        auto_scroll=False  # Desabilita rolagem automática para o final da lista ao adicionar itens — usuário mantém posição atual
    )

    # Bloco 04
    def add_task(e):  # Define a função de adicionar tarefa; 'e' é o ControlEvent — funciona como handler de Button.on_click e TextField.on_submit
        if task_input.value.strip() == "":  # Guard clause: verifica se o campo está vazio após remover espaços em branco — previne tarefas vazias
            return  # Encerra a função imediatamente sem executar o restante — early return evita lógica aninhada desnecessária
        task_text = task_input.value.strip()  # Armazena o texto limpo em variável local — chamamos strip() novamente para garantir consistência
        checkbox = ft.Checkbox(  # Cria o componente de marcação — cada tarefa tem seu próprio Checkbox independente
            label=task_text,  # O texto da tarefa é passado como label do Checkbox — exibido ao lado da caixa de marcação
            value=False  # Estado inicial desmarcado (False) — indica que a tarefa ainda não foi concluída
        )
        delete_button = ft.IconButton(  # Cria botão de ícone para excluir a tarefa — ícone sem texto, menor footprint visual que ElevatedButton
            icon=ft.Icons.DELETE,  # Usa o ícone DELETE do catálogo Material Icons do Flet — ícone de lixeira universalmente reconhecido
            icon_color=ft.Colors.RED,  # Cor vermelha reforça semântica de ação destrutiva — padrão de UX para ações de exclusão
            tooltip="Remover",  # Texto de dica exibido ao passar o mouse sobre o botão — melhora acessibilidade e usabilidade
            on_click=lambda e, item=None: remove_task(container)  # Lambda captura 'container' do escopo externo (closure) para saber qual item remover ao clicar
        )

        # Bloco 05
        container = ft.Container(  # Container envolve os dois componentes (checkbox + botão) adicionando estilos visuais ao item da lista
            content=ft.Row(  # Row posiciona checkbox e delete_button lado a lado no eixo horizontal dentro do Container
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # SPACE_BETWEEN: checkbox fica à esquerda e delete_button à direita, maximizando o espaço entre eles
                controls=[  # Lista de filhos do Row — a ordem determina a posição: checkbox primeiro (esq.), depois delete_button (dir.)
                    checkbox,  # Referência ao Checkbox criado anteriormente — inserido como primeiro filho do Row
                    delete_button  # Referência ao IconButton criado anteriormente — inserido como segundo filho do Row
                ]
            ),
            padding=10,  # 10px de espaçamento interno em todos os lados do Container — cria respiro visual ao redor do conteúdo
            border_radius=8,  # Arredonda os cantos do Container com raio de 8px — visual moderno, menos austero que cantos retos
            bgcolor=ft.Colors.BLUE_50  # Cor de fundo azul muito claro (50 = matiz mais suave) — diferencia visualmente cada item da lista
        )
        tasks.append(container)  # Adiciona o container na lista de estado Python — permite rastrear todos os itens independente da UI
        task_list.controls.append(container)  # Adiciona o container nos controles visuais do ListView — este append ainda não redesenha a tela
        task_input.value = ""  # Limpa o campo de texto após adicionar a tarefa — prepara para entrada da próxima tarefa
        page.snack_bar = ft.SnackBar(ft.Text("Tarefa adicionada!"))  # Cria um SnackBar (notificação temporária na parte inferior) confirmando visualmente a ação ao usuário
        page.snack_bar.open = True  # Define open=True para exibir o SnackBar — sem esta linha a notificação não apareceria
        page.update()  # Re-renderiza toda a página com o novo estado: campo limpo, novo item na lista e SnackBar visível

    # Bloco 06
    def remove_task(container):  # Recebe o Container específico a ser removido — a referência é passada pelo closure no lambda do delete_button
        if container in task_list.controls:  # Verifica se o container ainda existe na lista — evita ValueError caso o botão seja clicado mais de uma vez
            task_list.controls.remove(container)  # Remove o container da lista de controles visuais do ListView pelo operador de igualdade de referência
            page.snack_bar = ft.SnackBar(ft.Text("Tarefa removida!"))  # Cria novo SnackBar com mensagem de confirmação de remoção — diferente do texto de adição
            page.snack_bar.open = True  # Abre o SnackBar — deve ser definido como True explicitamente antes do page.update()
            page.update()  # Redesenha a UI sem o item removido e exibe o SnackBar de confirmação

    # Bloco 07
    add_button = ft.ElevatedButton(  # ElevatedButton tem sombra e maior destaque visual — apropriado para ação principal da tela
        "Adicionar",  # Primeiro argumento posicional é o texto do botão — argumento 'text' do construtor do ElevatedButton
        icon=ft.Icons.ADD,  # Ícone de adição (+) exibido à esquerda do texto — reforça visualmente a ação sem precisar ler o label
        on_click=add_task  # Referência à mesma função add_task — reutilização de lógica; funciona tanto via Enter quanto via clique
    )

    # Bloco 02
    page.add(  # page.add() aceita múltiplos controles separados por vírgula — todos são adicionados à página em sequência
    ft.AppBar(  # AppBar é a barra de navegação superior — no web gera uma barra fixa no topo da página
        title=ft.Text("Gerenciador de Tarefas"),  # Componente Text com o título da aplicação — ft.Text permite estilização rica (cor, tamanho, peso)
        center_title=True  # Centraliza o título horizontalmente na AppBar — padrão visual do Material Design para apps mobile
    ),
    ft.Column(  # Column principal da aplicação — empilha os três elementos do layout verticalmente
        width=600,  # Limita a largura a 600px para manter boa legibilidade — combinado com centralização da page
        controls=[  # Lista com os três filhos da Column na ordem vertical de exibição
            ft.Row(  # Row contém o TextField e o ElevatedButton lado a lado na parte superior
                controls=[task_input, add_button]  # task_input com expand=True ocupa o máximo de espaço; add_button fica à direita com tamanho fixo
            ),
            ft.Divider(),  # Linha horizontal de separação visual — divide a área de entrada da lista de tarefas abaixo
            task_list  # Referência ao ListView criado anteriormente — ocupará todo o espaço vertical restante (expand=True)
        ],
        expand=True  # A Column expande verticalmente para preencher a tela — sem isso o ListView não teria espaço para crescer
    )
)  # Fecha a chamada page.add() — a partir deste ponto todos os controles estão registrados e renderizados

ft.run(main)  # Inicia o runtime do Flet; view=WEB_BROWSER abre o app no navegador padrão em vez de janela nativa do SO
