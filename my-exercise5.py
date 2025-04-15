#  Ejercicio propuesto:
# Escribe una función que reciba una lista de palabras y retorne la palabra que aparece con más frecuencia. Si hay empate, retorna la que aparece primero.

# Ejemplo:
# most_common(["apple", "banana", "apple", "orange", "banana", "apple"])  
# # Output: "apple"

# ✨ Tips:
# Usa un diccionario para contar.
# Luego recorre la lista original (¡ojo! no el diccionario) para mantener el orden original y encontrar el más frecuente.

from collections import Counter

def most_common(arr):
    aux = Counter(arr)
    max_count = 0
    for i in arr:
        if aux[i] > max_count:
            max_count = aux[i]
            result = i

    return max_count, result
    

arr = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(most_common(arr))