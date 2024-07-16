#MENÚ VER MUSICA
def ver_musica():
    print("Mostrando toda la música disponible...")




#MENÚ VER MI LISTA DE CANCIONES
def ver_mi_lista():
    print("Mostrando tu lista de canciones...")



#MENÚ REPRODUCIR MIS CANCIONES
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