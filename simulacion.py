import numpy as np
import matplotlib.pyplot as plt

def simular_maquina_galton(num_canicas, num_niveles):
    resultados = np.zeros(num_niveles + 1, dtype=int)
    for _ in range(num_canicas):
        posicion = 0
        for _ in range(num_niveles):
            direccion = np.random.choice([-1, 1])  # -1 para la izquierda, 1 para la derecha
            posicion += direccion
        resultados[posicion] += 1
    return resultados

def graficar_histograma(resultados):
    plt.bar(range(len(resultados)), resultados, align='center')
    plt.xlabel('Contenedor')
    plt.ylabel('Cantidad de Canicas')
    plt.title('Simulación de Máquina de Galton')
    plt.show()

# Parámetros de la simulación
num_canicas = 3000
num_niveles = 12

# Simular y graficar
resultados_simulacion = simular_maquina_galton(num_canicas, num_niveles)
graficar_histograma(resultados_simulacion)
