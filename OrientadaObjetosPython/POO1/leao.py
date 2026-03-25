# leao.py

# Importa a classe Animal do arquivo animal.py
from animal import Animal

# Define a classe Leao que herda da classe Animal
class Leao(Animal):
    
    # Construtor da classe Leao
    def __init__(self, nome, idade, cor_juba):
        # Chama o construtor da superclasse (Animal) para inicializar nome e idade
        super().__init__(nome, idade)
        # Define o atributo privado específico da classe Leao: cor da juba
        self.Cor_juba = cor_juba

    # Getter para acessar a cor da juba
    def get_cor_juba(self):
        return self.Cor_juba  # Retorna o valor da cor da juba

    # Setter para modificar a cor da juba
    def set_cor_juba(self, cor):
        self.Cor_juba = cor  # Atualiza o valor da cor da juba

    # Sobrescreve o método emitir_som da classe Animal (polimorfismo)
    def emitir_som(self):
        return "O leão ruge: Rooooaaar!"  # Som característico do leão

    # Sobrescreve o método exibir_info da classe Animal
    def exibir_info(self):
        # Chama o método exibir_info da superclasse (Animal) e armazena o resultado
        base_info = super().exibir_info()
        # Retorna as informações completas do leão, incluindo a cor da juba
        return f"{base_info}\nCor da juba: {self.Cor_juba}"
