import matplotlib.pyplot as plt

def graficar(entradas, tiempos):
    plt.figure(figsize=(10, 6))
    #Grafica de lineas: plt.plot(entradas, tiempos, marker='o', linestyle='-', color='b', label='Tiempo de Ejecución')
    plt.bar(entradas, tiempos, color='skyblue', edgecolor='blue')
    plt.xlabel('Número de Elementos')
    plt.ylabel('Tiempo de Ejecución (segundos)')
    plt.title('Eficiencia de Inserción en LinkedList')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()