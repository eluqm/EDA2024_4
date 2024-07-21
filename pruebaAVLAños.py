from EstructurasDeDatos.TreeAVL import AVLTree
from leer_csv import leer_csv 

def main():
    archivo_csv = 'archive\\spotify_data.csv' 
    canciones = leer_csv(archivo_csv, 100)
    avlArbol = AVLTree()
    
    for cancion in canciones:
        avlArbol.insert(cancion.get_track_year())

    for cancion in canciones:
        print(cancion.get_track_year());

    print('Resultado de los años')
    print("In-order :", avlArbol.in_order())

if __name__ == "__main__":
    main()