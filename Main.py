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
    while True:
        print("\nMenú Ver mi Lista de Canciones")
        print("1. Listar mis canciones")
        print("2. Agregar una Canción a mi lista")
        print("3. Eliminar una Canción de mi lista")
        print("4. Ordenar mi lista")
        print("5. Buscar canción")
        print("6. Salir")
        
        opcion = input("Elige una opción: ")
        reproductor = Reproductor()
         
        if opcion == '1':
            n = int(input("Se listan sus canciones"))
            reproductor.listar_mis_canciones(n)
        elif opcion == '2':
            n = int(input("Se agrega una cancion a la lista "))
            reproductor.agregar_cancion(n)
        elif opcion == '3':
            n = int(input("Se elimina una cancion de la lista "))
            reproductor.eliminar_cancion(n)
        elif opcion == '4':
            n = int(input("Ordenar mi lista: "))
            reproductor.ordenar_lista(n)
        elif opcion == '5':
            nombre = input("Buscar cancion: ")
            reproductor.buscar_cancion(nombre)
        elif opcion == '6':
            print("Saliendo del menú Ver mi lIsta de Canciones  ...")
            break
        else:
            print("Opción no válida, por favor elige de nuevo.")




        ########## <<<<<REPRODUCIR MIS CANCIONES >>>>> ########## 
def reproducir_mis_canciones():
    while True:
        print("\nMenú Ver mi Lista de Canciones")
        print("1. Reproducir mis Canciones")
        print("2. Cambiar orden de dos canciones")
        print("3. Salir")
        
        opcion = input("Elige una opción: ")
        reproductor = Reproductor()
         
        if opcion == '1':
            n = int(input("Se reproducen las canciones"))
            reproductor.listar_mis_canciones(n)
        elif opcion == '2':
            n = int(input("Se cambia el orden de dos canciones "))
            reproductor.agregar_cancion(n)
        elif opcion == '3':
            print("Saliendo del menú Reproducir mis canciones  ...")
            break
        else:
            print("Opción no válida, por favor elige de nuevo.")


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