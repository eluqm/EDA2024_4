import random
from leer_csv import leer_csv

class Reproductor:
    def listar_n_aleatorio(self, n):
        print(f"\nListando {n} primeras canciones de forma aleatoria:")
        canciones = leer_csv('archive/spotify_data.csv', n)
        
        for i, cancion in enumerate(canciones, start=1):
            print(f"{i}. {cancion}")
        

    def listar_n_ano(self, n):
        print(f"Listando {n} primeras canciones por año:")
        # Implementar lógica aquí
        pass

    def listar_n_duracion(self, n):
        print(f"Listando {n} primeras canciones por duración:")
        # Implementar lógica aquí
        pass

    def listar_n_artista(self, n):
        print(f"Listando {n} primeras canciones por artista:")
        # Implementar lógica aquí
        pass

    def listar_por_nombre(self, nombre):
        print(f"Listando canciones con el nombre '{nombre}':")
        # Implementar lógica aquí
        pass