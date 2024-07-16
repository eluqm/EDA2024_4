from reproductor import Reproductor

                ########## <<<<<MENÚ VER MUSICA >>>>>########## 
def ver_musica():
    while True:
        print("\nMenú Ver Música")
        print("1. Listar 'n' primeras canciones de forma aleatoria")
        print("2. Listar 'n' primeras canciones por año")
        print("3. Listar 'n' primeras canciones por duración")
        print("4. Listar 'n' primeras canciones por artista")
        print("5. Listar por nombre de canción")
        print("6. Salir")
        
        opcion = input("Elige una opción: ")
        reproductor = Reproductor()
         
        if opcion == '1':
            n = int(input("Introduce el número de canciones a listar: "))
            reproductor.listar_n_aleatorio(n)
        elif opcion == '2':
            n = int(input("Introduce el número de canciones a listar: "))
            reproductor.listar_n_ano(n)
        elif opcion == '3':
            n = int(input("Introduce el número de canciones a listar: "))
            reproductor.listar_n_duracion(n)
        elif opcion == '4':
            n = int(input("Introduce el número de canciones a listar: "))
            reproductor.listar_n_artista(n)
        elif opcion == '5':
            nombre = input("Introduce el nombre de la canción: ")
            reproductor.listar_por_nombre(nombre)
        elif opcion == '6':
            print("Saliendo del menú Ver Música...")
            break
        else:
            print("Opción no válida, por favor elige de nuevo.")




        ########## <<<<<MENÚ VER MI LISTA DE CANCIONES >>>>> ########## 
def ver_mi_lista():
    print("Mostrando tu lista de canciones...")



        ########## <<<<<REPRODUCIR MIS CANCIONES >>>>> ########## 
def reproducir_mis_canciones():
    print("Reproduciendo tus canciones...")





#MENÚ PRINCIPAL DE LA APLICACIÓN
def main():
    while True:
        print("\nMenú")
        print("1. Ver música")
        print("2. Ver mi lista de canciones")
        print("3. Reproducir mis canciones")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")
        if opcion == '1':
            ver_musica()
        elif opcion == '2':
            ver_mi_lista()
        elif opcion == '3':
            reproducir_mis_canciones()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor elige de nuevo.")

if __name__ == "__main__":
    main()