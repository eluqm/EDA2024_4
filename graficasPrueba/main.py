from medirTiempo import medir_tiempo_insercion
from graficarTiempo import graficar
import numpy as np

def main():
    # Lista de números de elementos para probar
    numeros_de_elementos = np.arange(1, 9001, 100)  # Por ejemplo, 100, 200, ..., 1000
    tiempos = []

    for num_elementos in numeros_de_elementos:
        elementos = list(range(num_elementos))  # Generar una lista de elementos
        tiempo = medir_tiempo_insercion(elementos)
        tiempos.append(tiempo)
    
    graficar(numeros_de_elementos, tiempos)

if __name__ == "__main__":
    main()