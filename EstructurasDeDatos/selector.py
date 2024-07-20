import random
class Selector:
    def __init__(self, canciones):
        self.galeria = canciones

    def selectorMusics(self, numero):
        songsSelect = []
        indices_seleccionados = set()

        while len(songsSelect) < numero:
            indice_aleatorio = random.randint(0, len(self.galeria) - 1)
            if indice_aleatorio not in indices_seleccionados:
                indices_seleccionados.add(indice_aleatorio)
                songsSelect.append(self.galeria[indice_aleatorio])

        return songsSelect
        