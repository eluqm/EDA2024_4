import numpy as np
import matplotlib.pyplot as plt
from medirTiempoQueue import medir_tiempo_insercion # Asegúrate de que la ruta sea correcta

def main():
    numeros_de_elementos = np.arange(1, 40001, 100)  
    tiempos = []

    for num_elementos in numeros_de_elementos:
        elementos = list(range(num_elementos))
        tiempo = medir_tiempo_insercion(elementos)
        tiempos.append(tiempo)

    plt.figure(figsize=(10, 6))
    plt.bar(numeros_de_elementos, tiempos, color='skyblue', edgecolor='blue')
    plt.xlabel('Número de Elementos')
    plt.ylabel('Tiempo de Ejecución (segundos)')
    plt.title('Eficiencia de Inserción en Queue')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

if __name__ == "__main__":
    main()