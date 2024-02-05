class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def novo_nome(self, novo_nome):
        self._nome = novo_nome.title

    @property
    def ano(self):
        return self._ano


    @property
    def likes(self):
        return self._likes

    @likes.setter
    def dar_likes(self):
        self.likes += 1

