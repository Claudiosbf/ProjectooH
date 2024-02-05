import programa


class Serie(programa.Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.__temporadas = temporadas


    @property
    def temporadas(self):
        return self.__temporadas


atlanta = Serie('Atlanta', 2018, 2)
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano}'
      f' - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')






