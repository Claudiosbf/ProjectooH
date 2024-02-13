import programa


class Filme(programa.Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self._duracao = duracao


    @property
    def duracao(self):
            return self._duracao

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self._ano} - Duração: {self._duracao} - Likes: {self._likes}'

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
#print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano}'
 #     f' - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')

