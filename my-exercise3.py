# 🔴 Ejercicio 3 (Avanzado) – Subarreglo de Suma Máxima (Divide & Conquer vs. Kadane)
# Enunciado:
# Dado un arreglo de enteros (positivos y negativos), implementa una función que devuelva la suma del subarreglo contiguo de suma máxima.
# NOTA1: Un subarreglo contiguo es una parte del arreglo original que toma elementos consecutivos, sin saltarse ninguno. 
# NOTA2: ¿Qué es la suma máxima de un subarreglo contiguo? Es encontrar el subarreglo contiguo que, al sumar sus elementos, te dé el mayor resultado posible.
# Primero resuélvelo con el algoritmo de Divide and Conquer, y luego con el algoritmo de Kadane.
# Analiza y compara sus complejidades.

# I) ESTA ES MI RESOLUCIÓN-----------------------------------------------------------------------------------
# Primero hay que encontrar todos los subarreglos contiguos posibles.

def subarreglos(arr):
    subarr = [] #Inicializamos un arreglo de subarreglos vacio
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            subarr.append(arr[i:j+1]) # Agregamos al subarr una porción del arr que va desde i hasta j+1. Notacion slice i: j+1
    
# Luego, hay calcular la suma de cada uno de los subarreglos contiguos encontrados.
    sub_sum=[]
    for j in subarr:
        sub_sum.append(sum(j)) # aca agregamos la suma de cada subarreglo contiguo a un nuevo arreglo sub_sum. Notacion sum(j)

# Finalmente, hay que encontrar el subarreglo contiguo con la suma máxima.
    max_sum = max(sub_sum) # Aca descubrimos cual es la suma máxima
    max_index = sub_sum.index(max_sum) # Aca decubrimos el index de esa suma máxima dentro de sub_sum
    max_subarr = subarr[max_index] # Aca llamamos al subarreglo usando el indice recien encontrado.
    
    return f"Esta la suma máxima: {max_sum}. Este es el subarreglo: {max_subarr}"

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(subarreglos(arr)) # Imprimimos el arreglo de subarreglos contiguos


# II) USANDO KADANE-----------------------------------------------------------------------------------

def sub_kadane(arr):
    max_current = arr[0]
    max_global = arr[0]
    for i in arr:
        max_current = max(i, max_current + i)
        max_global = max(max_global, max_current)

    return max_global

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(f"Esta es la segunda solución usando Kadane: {sub_kadane(arr)}")



# RESOLUCIÓN DIVIDE AND CONQUER-----------------------------------------------------
# El coste de este algoritmo sería O(n2) en el primer bucle ya que es anidado. 
# Luego en el segundo bucle tenemos el arreglo de subarreglos egenrado en el primero, esto seria una especie de tercer bucle anidado, por lo que el coste seria O(n3).
# Posteriormente, las funciones max() e index() trabajan sobre un arreglo de tamaño O(n²), por lo que ambas tienen coste O(n²). 
# Sin embargo, este coste es menor en orden de magnitud que el anterior, por lo tanto, el coste total del algoritmo sigue siendo O(n³).
# Coste total del algoritmo es O(n3) + O(n2) = O(n3).
# Esto se cunple para todos los casos ya que siempre se debe hacer las mismas iteraciones, no hay una condicion para no hacerlas.