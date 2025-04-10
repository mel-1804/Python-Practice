# Ejercicio 1 (Básico) – Frecuencia de Caracteres
# Enunciado:
# Dado un string, implementa una función que cuente la frecuencia de cada carácter y lo devuelva como un diccionario.
# Ordena el resultado en orden descendente de frecuencia.
# Bonus: Usa collections.Counter.

# I) ESTA FUE MI SOLUCION-------------------------------------------------------------------------------------------------------------------
# from collections import Counter

# # 1) Primero mandamos los caracteres del string a un diccionario
# def contar_freq(string):
#     aux = {}
   
#     for char in string:
#         aux[char] = aux.get(char, 0) + 1
#     return aux

# #2) Luego ordenamos el diccionario por frecuencia
# def ordenar_freq(aux):
#     return sorted(aux.items(), key=lambda x: x[1], reverse=True)

# ii) ESTA RESPUESTA ES LA QUE ME SOPLÓ LA IA----------------------------------------------------------------------------------------------

# from collections import Counter

# def contar_freq(string):
#     return Counter(string)

# def orde_freq(aux):
#     return sorted(aux.items(), key=lambda x: x[1], reverse=True)        

# string = "hello world"
# print(orde_freq(contar_freq(string)))


# ESTA ES OTRA SOLUCION BASADA EN LA SEGUNDA PERO MAS DIRECTA---------------------------------------------------------------------------------

from collections import Counter

def contar_freq(string):
    aux = Counter(string)
    aux2 = sorted(aux.items(), key=lambda x: x[1], reverse=True)        
    return aux2

string = "hello world"
print(contar_freq(string))


# HICIMOS 2 FUNCIONES SEPARADAS Y COMPLEMENTE INDEPENDIENTES, UNA PASA LOS DATOS DE LA LISTA A UN DICCIONARIO SIN NOMBRE, LA OTRA ORDENA EL DICCIONARIO USANDO UNA FUNCION LAMBDA.
# LA SINTAXIS DE .sorted() ES: sorted(iterable, key=None, reverse=False)
# LA SINTAXIS DE .items() ES: dict.items() # Devuelve una vista de los pares clave-valor del diccionario.
# LA SINTAXIS DE .get() ES: dict.get(key[, default]) # Devuelve el valor de la clave especificada. Si la clave no existe, devuelve el valor predeterminado (None si no se proporciona).
# LUEGO, EL LINEA FINAL CUANO HACEMOS EL PRINT RELACIONAMOS EL RESULTADO DE LA PRIMERA FUNCION (UN DICCIONARIO) PASANDOLO COMO PARAMETRO DE LA SEGUNDA FUNCION.

# AHORA ANALICEMOS EL COSTE DE ESTE ALGORITMO-------------------------------------------------------------------------------------------------
# La primera parte de la función, que utiliza Counter(string), tiene un coste de tiempo O(n), ya que recorre cada carácter del string exactamente una vez, sin importar su contenido, longitud u orden. 
# Este comportamiento se mantiene constante en los tres escenarios: mejor caso, peor caso y caso promedio, todos con complejidad O(n).
# La segunda función de ordenamiento desglosa su coste como sigue:
#       .items() → Esto genera una lista de tamaño ≤ n (como máximo 26 si son letras del alfabeto, o hasta 128 para ASCII), pero en notación general es O(k), donde k es el número de claves únicas (como n en el peor caso).
#       .sorted(..., key=...) → O(k log k) Ordenar una lista de k pares (carácter, frecuencia) según su frecuencia (el segundo elemento de la tupla).
# CONCLUSIÓN:
# Tiempo total del algoritmo: O(n + k log k)
# En el peor caso, si todos los caracteres son únicos (k = n), esto se vuelve O(n log n).

