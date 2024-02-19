import programa


class Serie(programa.Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self._temporadas = temporadas


    @property
    def temporadas(self):
        return self._temporadas

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self._ano} - Temporadas: {self._temporadas} - Likes: {self._likes}'


atlanta= Serie('Atlanta', 2018, 2)
demolidor = Serie('Demolidor', 2016, 2)






