# Ejercicio: Encuentra el primer carácter no repetido
# Enunciado: Escribe una función en Python que reciba un string y devuelva el primer carácter que no se repite. Si todos los caracteres se repiten, devuelve None.

# 🧪 Ejemplos:
# >>> first_unique_char("abracadabra")
# 'c'

# >>> first_unique_char("aabbcc")
# None

# >>> first_unique_char("stress")
# 't'

# 🎯 Objetivo:
# Usar estructuras como diccionarios o collections.Counter
# Aplicar control de flujo
# Pensar en eficiencia (idealmente O(n))

# 💡 Pista:
# Puedes recorrer el string una vez para contar las apariciones, y otra vez para identificar el primero con conteo 1.

#I) ESTA ES MI SOLUCIÓN-----------------------------------------------------------------------------------
from collections import Counter

def first_uniq(string):
    freq = Counter(string)
    
    for char in string:
        if freq[char] == 1:
            return char
    return None
    
string = "abbracadabra"
print(first_uniq(string))

# Creamos un diccionario usando Counter, que cuenta la frecuencia de cada carácter en el string.
# Luego iteramos sobre el string pero en la condición del if usamos el diccionario creado anteriormente para ver si el valor de la clave es 1, si es así, devolvemos el carácter.
# El coste es O(n) porque recorremos el string dos veces, pero no anidado