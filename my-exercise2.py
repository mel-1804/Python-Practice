# 🟡 Ejercicio 2 (Intermedio) – Ordenamiento Personalizado (Counting Sort Adaptado)
# Enunciado:
# Dado un arreglo de enteros del 0 al 100, implementa una función que lo ordene usando Counting Sort.
# Hazlo sin usar funciones de ordenamiento de Python.
# Bonus: Devuelve también el número de comparaciones realizadas, aunque Counting Sort no hace comparaciones en su lógica principal.

# I) ESTA FUE MI SOLUCION-------------------------------------------------------------------------------------------------------------------

# def counting_sort(arr):
#     # se trabaja con 3 arreglos a, b y c, en este caso arr, output y aux respectivamente. i, j y k son indices de cada uno de los arreglos.

#     aux = [0]*101  
#     output = [0]*len(arr) 

# # Primero, la lista aux contiene las frecuencias de cada número en arr.
#     for i in arr:
#         aux[i] = aux[i] + 1

# # Luego, la lista aux contiene frecucencias acumuladas de cada número en arr.
#     for k in range(1, len(aux)):
#         aux[k] = aux[k] + aux[k - 1]

# # Por último, output sera rellanado con el resultado final.
#     for i in range(len(arr) - 1, -1, -1):
#         output[aux[arr[i]] - 1] = arr[i]
#         aux[arr[i]] = aux[arr[i]] - 1

#     return output


# arr = [4, 2, 2, 8, 3, 3, 1, 5, 5, 18, 25, 25, 40, 99, 5, 25, 41, 69]
# print(counting_sort(arr))

# ESTA ES LA SOLUCION CON EL EXTRA DE DEVOLVER NRO DE COMPARACIONES------------------------------------------------------------

def counting_sort(arr):
    # se trabaja con 3 arreglos a, b y c, en este caso arr, output y aux respectivamente. i, j y k son indices de cada uno de los arreglos.

    aux = [0]*101  
    output = [0]*len(arr) 
    operations = 0  # Inicializamos el contador de comparaciones u operaciones

# Primero, la lista aux contiene las frecuencias de cada número en arr.
    for i in arr:
        aux[i] = aux[i] + 1
        operations += 1  # Contamos la operación de asignación

# Luego, la lista aux contiene frecucencias acumuladas de cada número en arr.
    for k in range(1, len(aux)):
        aux[k] = aux[k] + aux[k - 1]
        operations += 1  # Contamos la operación de asignación

# Por último, output sera rellanado con el resultado final.
    for i in range(len(arr) - 1, -1, -1):
        output[aux[arr[i]] - 1] = arr[i]
        aux[arr[i]] = aux[arr[i]] - 1
        operations += 1 # Contamos la operación de asignación

    return output, operations


arr = [4, 2, 2, 8, 3, 3, 1, 5, 5, 18, 25, 25, 40, 99, 5, 25, 41, 69]
print(counting_sort(arr))

# ARRAYS INICIALIZADOS CON 0?
# En Python, al inicializar un array con 0 como en aux = [0]*101, se crea una lista de longitud 101 (de 0 a 100 son 101 numeros) donde cada elemento es 0.
# Esto es útil para contar frecuencias o inicializar valores en algoritmos de ordenamiento como Counting Sort.
# Antes de iterar sobre el array original, todo courre 0 veces, luego encima de eso vas sumando ocurrencias.
# El array aux va desde 1 a 101 porque entramos números del 0 al 100, y el índice 0 se deja vacío para facilitar el conteo.
# En el caso del array output vas desde 0 a len(arr) porque dentro de este array mostraremos los mismos números que hay en el array original, pero ordenados.

# PRIMER BUCLE for i in arr:
# Recorremos con los valores del bucle, no con sus indices, por eso no es necesario escribir expresiones como aux[ar[i]], sino directamente aux[i].

# SEGUNDO BUCLE for k in range(1, len(aux)):
# Recorremos los indices de aux, no sus valores. Sumamos elementos contiguos para hacer la suma o frecuencia acumulada aux[k] + aux[k - 1].

# TERCER BUCLE for i in range(len(arr) - 1, -1, -1):
# Recorremos el array arr desde el último elemento hasta el primero, por eso el -1, disminuyendo el índice en 1 cada vez.
# Aca la expresión aux[ar[i]] tiene sentido, porque las i son indices de arr, y los valores de arr son los indices de aux.



# COSTE DEL ALGORITMO-------------------------------------------------------------------------------------
# El algoritmo Counting Sort tiene una complejidad de O(n + k), donde n es el número de elementos en el arreglo de entrada y k es el rango de los números (en este caso, 101).
# Este tipo de algoritmos se caracteriza por tener un coste lineal en el mejor, peor y promedio de los casos, lo que lo hace muy eficiente para arreglos con un rango limitado de valores.

