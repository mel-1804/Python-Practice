# Ejercicio propuesto:
# Escribe una función en Python que reciba una lista de palabras y devuelva un diccionario donde las claves sean las palabras, y los valores cuántas veces aparece cada palabra.

# 🚫 No uses Counter()
# ✅ Hazlo usando un bucle for y un diccionario vacío

# 🧪 Ejemplo:
# word_count(["apple", "banana", "apple", "orange", "banana", "apple"])


# 🟰 Output:
# {"apple": 3, "banana": 2, "orange": 1}

# 💻 Plantilla del código:


def word_count(words):
    count_dict = {}  # creas un diccionario vacío
    for word in words:
        count_dict[word] = count_dict.get(word, 0) + 1   # ...suma 1 al valor

    return count_dict

words= ["apple", "banana", "apple", "orange", "banana", "apple"]
print(word_count(words))
