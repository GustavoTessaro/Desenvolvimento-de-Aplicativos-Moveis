# # main.py

# # Importa as classes Leao e Elefante de seus respectivos módulos
# from leao import Leao
# from elefante import Elefante

# # Função principal do programa
# def main():
#     # Exibe um cabeçalho inicial
#     print("=== Cadastro de Animais do Zoológico ===")

#     # Solicita ao usuário o tipo de animal e converte para minúsculas, 
#     # removendo espaços extras
#     tipo = input("Digite o tipo de animal (leao/elefante): ").strip().lower()

#     # Verifica se o tipo informado é válido
#     if tipo not in ["leao", "elefante"]:
#         print("Tipo inválido. Use 'leao' ou 'elefante'.")
#         return  # Encerra a função se o tipo for inválido

#     # Solicita o nome do animal
#     nome = input("Nome do animal: ").strip()

#     # Solicita a idade do animal
#     idade = input("Idade do animal: ").strip()

#     # Valida se a idade é um número inteiro
#     if not idade.isdigit():
#         print("Erro: idade deve ser um número inteiro.")
#         return  # Encerra a função se a idade for inválida

#     # Converte a idade de string para inteiro
#     idade = int(idade)

#     # Verifica se o tipo é "leao" e coleta informações específicas
#     if tipo == "leao":
#         # Solicita a cor da juba
#         cor_juba = input("Cor da juba: ").strip()
#         # Cria um objeto da classe Leao com os dados fornecidos
#         animal = Leao(nome, idade, cor_juba)

#     # Se for um elefante, coleta informações específicas
#     elif tipo == "elefante":
#         # Solicita o tamanho das orelhas
#         tamanho_orelhas = input("Tamanho das orelhas (em cm): ").strip()

#         # Verifica se o valor é numérico
#         if not tamanho_orelhas.isdigit():
#             print("Erro: o tamanho das orelhas deve ser um número.")
#             return  # Encerra a função se o valor for inválido

#         # Cria um objeto da classe Elefante com os dados fornecidos
#         animal = Elefante(nome, idade, int(tamanho_orelhas))

#     # Exibe as informações do animal
#     print("\n=== Informações do Animal ===")
#     print(animal.exibir_info())  # Chama método que retorna dados formatados
#     print(animal.emitir_som())   # Chama método que retorna o som do animal (polimorfismo)

# # Executa a função main apenas se este arquivo for executado diretamente (não importado como módulo)
# main()

# Importações necessárias
import tkinter as tk  # Importa a biblioteca tkinter para criar interfaces gráficas
from tkinter import messagebox  # Importa o módulo messagebox para exibir caixas de diálogo (alertas, erros, informações)
from leao import Leao  # Importa a classe Leao do arquivo leao.py
from elefante import Elefante  # Importa a classe Elefante do arquivo elefante.py

def cadastrar_animal():
    """Função chamada quando o botão 'Cadastrar' é clicado"""
    tipo = tipo_var.get().lower()  # Obtém o valor selecionado no menu e converte para minúsculas
    nome = entry_nome.get().strip()  # Obtém o texto do campo nome e remove espaços em branco das extremidades
    idade = entry_idade.get().strip()  # Obtém o texto do campo idade e remove espaços em branco das extremidades

    # Validação do tipo de animal
    if tipo not in ["leao", "elefante"]:  # Verifica se o tipo selecionado é válido
        messagebox.showerror("Erro", "Selecione um tipo válido: Leão ou Elefante.")  # Exibe uma caixa de erro
        return  # Interrompe a execução da função

    # Validação do nome
    if not nome:  # Verifica se o campo nome está vazio (após remover espaços)
        messagebox.showerror("Erro", "Digite o nome do animal.")  # Exibe uma caixa de erro
        return  # Interrompe a execução da função

    # Validação da idade
    if not idade.isdigit():  # Verifica se a idade contém apenas dígitos (números)
        messagebox.showerror("Erro", "A idade deve ser um número inteiro.")  # Exibe uma caixa de erro
        return  # Interrompe a execução da função

    idade = int(idade)  # Converte a string idade para número inteiro

    # Processamento específico para cada tipo de animal
    if tipo == "leao":  # Se o tipo selecionado for leão
        cor_juba = entry_extra.get().strip()  # Obtém a cor da juba do campo extra
        if not cor_juba:  # Verifica se o campo cor da juba está vazio
            messagebox.showerror("Erro", "Digite a cor da juba.")  # Exibe uma caixa de erro
            return  # Interrompe a execução da função
        animal = Leao(nome, idade, cor_juba)  # Cria um objeto da classe Leao com os dados informados

    elif tipo == "elefante":  # Se o tipo selecionado for elefante
        tamanho = entry_extra.get().strip()  # Obtém o tamanho das orelhas do campo extra
        if not tamanho.isdigit():  # Verifica se o tamanho contém apenas dígitos
            messagebox.showerror("Erro", "O tamanho das orelhas deve ser numérico.")  # Exibe uma caixa de erro
            return  # Interrompe a execução da função
        animal = Elefante(nome, idade, int(tamanho))  # Cria um objeto da classe Elefante com os dados informados

    # Exibe as informações do animal cadastrado
    messagebox.showinfo("Animal Cadastrado", f"{animal.exibir_info()}\n{animal.emitir_som()}")  # Mostra uma caixa de informação com os dados do animal e seu som

def atualizar_rotulo_extra(*args):
    """Função chamada automaticamente quando o tipo de animal é alterado no menu"""
    tipo = tipo_var.get().lower()  # Obtém o tipo selecionado e converte para minúsculas
    if tipo == "leao":  # Se leão foi selecionado
        label_extra.config(text="Cor da juba:")  # Altera o texto do rótulo extra para "Cor da juba:"
    elif tipo == "elefante":  # Se elefante foi selecionado
        label_extra.config(text="Tamanho das orelhas (cm):")  # Altera o texto do rótulo extra para "Tamanho das orelhas (cm):"
    else:  # Se nenhum tipo válido foi selecionado
        label_extra.config(text="")  # Deixa o rótulo extra vazio

# Configuração da janela principal
janela = tk.Tk()  # Cria a janela principal da aplicação usando tkinter
janela.title("Cadastro de Animais do Zoológico")  # Define o título que aparece na barra superior da janela
janela.geometry("350x150")  # Define o tamanho da janela em pixels (largura x altura)

# Widgets de entrada
tk.Label(janela, text="Tipo de animal:").grid(row=0, column=0, sticky="e")  # Cria um rótulo (label) na linha 0, coluna 0, alinhado à direita (sticky="e" = east)
tipo_var = tk.StringVar()  # Cria uma variável especial do tkinter para armazenar o valor selecionado no menu
tipo_var.trace_add("write", atualizar_rotulo_extra)  # Adiciona um "observador" que chama a função atualizar_rotulo_extra sempre que tipo_var for modificada (write)
tipo_menu = tk.OptionMenu(janela, tipo_var, "leao", "elefante")  # Cria um menu suspenso com as opções "leao" e "elefante"
tipo_menu.grid(row=0, column=1)  # Posiciona o menu na linha 0, coluna 1

tk.Label(janela, text="Nome:").grid(row=1, column=0, sticky="e")  # Cria rótulo "Nome:" na linha 1, coluna 0, alinhado à direita
entry_nome = tk.Entry(janela)  # Cria um campo de entrada de texto para o nome do animal
entry_nome.grid(row=1, column=1)  # Posiciona o campo de entrada na linha 1, coluna 1

tk.Label(janela, text="Idade:").grid(row=2, column=0, sticky="e")  # Cria rótulo "Idade:" na linha 2, coluna 0, alinhado à direita
entry_idade = tk.Entry(janela)  # Cria um campo de entrada de texto para a idade do animal
entry_idade.grid(row=2, column=1)  # Posiciona o campo de entrada na linha 2, coluna 1

label_extra = tk.Label(janela, text="")  # Cria um rótulo vazio que será preenchido dinamicamente baseado no tipo de animal selecionado
label_extra.grid(row=3, column=0, sticky="e")  # Posiciona o rótulo extra na linha 3, coluna 0, alinhado à direita
entry_extra = tk.Entry(janela)  # Cria um campo de entrada adicional para informações específicas do animal
entry_extra.grid(row=3, column=1)  # Posiciona o campo de entrada extra na linha 3, coluna 1

# Botão de envio
tk.Button(janela, text="Cadastrar", command=cadastrar_animal).grid(row=4, columnspan=2, pady=10)  # Cria botão "Cadastrar" que chama a função cadastrar_animal quando clicado, ocupa 2 colunas (columnspan=2) e tem espaçamento vertical (pady=10)

# Inicia o loop da interface
janela.mainloop()  # Inicia o loop principal da interface gráfica - mantém a janela aberta e responsiva aos eventos do usuário