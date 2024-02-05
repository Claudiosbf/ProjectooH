import programa


class Filme(programa.Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.__duracao = duracao


    @property
    def duracao(self):
            return self.__duracao

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano}'
      f' - Temporadas: {vingadores.duracao} - Likes: {vingadores.likes}')

