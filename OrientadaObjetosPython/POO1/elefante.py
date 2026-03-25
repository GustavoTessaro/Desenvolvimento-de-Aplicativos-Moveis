# elefante.py

from animal import Animal

class Elefante(Animal):
    def __init__(self, nome, idade, tamanho_orelhas):
        super().__init__(nome, idade)
        self.Tamanho_orelhas = tamanho_orelhas

    def get_tamanho_orelhas(self):
        return self.Tamanho_orelhas

    def set_tamanho_orelhas(self, tamanho):
        self.Tamanho_orelhas = tamanho

    def emitir_som(self):
        return "O elefante faz trombeta: Prrruuuu!"

    def exibir_info(self):
        base_info = super().exibir_info()
        return f"{base_info}\nTamanho das orelhas: {self.Tamanho_orelhas} cm"
