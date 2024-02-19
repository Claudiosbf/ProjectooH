import filme
import serie

class Playlist:
   def __init__(self, nome, programas):
      self._nome = nome
      self._programas = programas

   def __getitem__(self, item):
      return self._programas[item]



   @property
   def nome(self):
      return self._nome

   def __len__(self):
      return len(self._programas)

filmes_e_series = [filme.vingadores, serie.atlanta, serie.demolidor, filme.tmep]
playlist_fim_de_semana = Playlist("Fim de semana", filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
   print(programa)
