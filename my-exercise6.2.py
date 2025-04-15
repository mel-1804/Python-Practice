# Ejercicio propuesto:
# Escribe una función en Python que reciba una lista de palabras y devuelva un diccionario donde las claves sean las palabras, y los valores cuántas veces aparece cada palabra.

# 🚫 No uses Counter()
# ✅ Hazlo usando un bucle for y un diccionario vacío

# 🧪 Ejemplo:
# word_count(["apple", "banana", "apple", "orange", "banana", "apple"])


# 🟰 Output:
# {"apple": 3, "banana": 2, "orange": 1}

# 💻 Plantilla del código:

from collections import defaultdict # Importamos defaultdict para evitar la verificación de claves

def word_count(words):
    count_dict = defaultdict(int)  # Usamos defaultdict para inicializar automáticamente con 0
    for word in words:
        count_dict[word] += 1

    return count_dict
    

words= ["apple", "banana", "apple", "orange", "banana", "apple"]
print(word_count(words))
