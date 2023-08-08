# Importamos las bibliotecas que vamos a utilizar.
# numpy: es una biblioteca para trabajar con matrices y operaciones matemáticas en Python.
# random: es una biblioteca para generar números aleatorios.
# matplotlib.pyplot: es una biblioteca para crear visualizaciones como gráficos.
# codecademylib3: parece ser una biblioteca específica de Codecademy (es posible que no la necesites si no estás en esa plataforma).
import numpy as np
import random
import matplotlib.pyplot as plt
#import codecademylib3

# Aquí hay comentarios para el usuario, sugiriendo que cambie los valores de 'samp_size' y 'pop_stdev' 
# y vuelva a ejecutar el código para ver diferentes resultados.
# samp_size representa el tamaño de la muestra que queremos tomar de la población.
# pop_stdev representa la desviación estándar de la población.
samp_size = 200
pop_stdev = 30

# Aquí estamos creando una población de 100,000 valores.
# Estos valores siguen una distribución normal (también conocida como distribución gaussiana) con una media de 10 y una 
# desviación estándar especificada por 'pop_stdev'.
# 'loc' es el centro de la distribución (es decir, la media) y 'scale' es la desviación estándar.
population = np.random.normal(loc = 10, scale = pop_stdev, size = 100000)

# Convertimos la matriz 'population' a una lista.
population = list(population)

# Creamos una lista vacía llamada 'sample_means' donde almacenaremos las medias de las muestras que tomemos.
sample_means = []

# Iniciamos un bucle que se ejecutará 10,000 veces.
for i in range(10000):
    # En cada iteración, tomamos una muestra aleatoria de la 'population' de tamaño 'samp_size'.
    samp = random.sample(population, samp_size)
    # Calculamos la media de esta muestra y la añadimos a nuestra lista 'sample_means'.
    sample_means.append(np.mean(samp))

# Usamos matplotlib para visualizar las medias de las muestras en un histograma.
plt.hist(sample_means, bins = 30)
# Añadimos un título al histograma.
plt.title('Sampling Distribution')
# Establecemos los límites del eje x para el gráfico.
plt.xlim(-10, 30)

# Finalmente, mostramos el gráfico.
plt.show()

# Para depurar el código:
# 1. Utiliza 'print()' para mostrar los valores de las variables y asegúrate de que son lo que esperas.
# 2. Puedes utilizar la herramienta pdb (Python Debugger) insertando 'import pdb; pdb.set_trace()' en cualquier parte del código.
#    Esto detendrá la ejecución y te permitirá inspeccionar las variables y el flujo del programa paso a paso.
