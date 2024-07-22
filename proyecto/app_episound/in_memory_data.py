# in_memory_data.py
class Cancion:
    def __init__(self, titulo, artista, album, duracion):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracion = duracion

# Crear una instancia de Cancion
cancion = Cancion(
    titulo="Bohemian Rhapsody",
    artista="Queen",
    album="A Night at the Opera",
    duracion="5:55"
)