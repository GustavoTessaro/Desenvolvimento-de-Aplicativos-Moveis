# animal.py

# Define a classe Animal — essa é uma classe base (superclasse) para outros animais
class Animal:
    
    # Método construtor da classe, executado ao criar um objeto Animal
    def __init__(self, nome, idade):
        self.Nome = nome    # Atributo privado: nome do animal
        self.Idade = idade  # Atributo privado: idade do animal

    # Método de acesso (getter) para o nome
    def get_nome(self):
        return self.Nome    # Retorna o nome do animal

    # Método de modificação (setter) para o nome
    def set_nome(self, nome):
        self.Nome = nome    # Atualiza o nome do animal

    # Método de acesso (getter) para a idade
    def get_idade(self):
        return self.Idade   # Retorna a idade do animal

    # Método de modificação (setter) para a idade
    def set_idade(self, idade):
        self.Idade = idade  # Atualiza a idade do animal

    # Método que simula o som emitido por um animal genérico
    # Este método poderá ser sobrescrito pelas subclasses (polimorfismo)
    def emitir_som(self):
        return "Som genérico de animal."  # Valor padrão

    # Método que retorna as informações do animal de forma formatada
    def exibir_info(self):
        return f"Nome: {self.Nome}\nIdade: {self.Idade} anos"

