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

    for word in words:  # recorres cada palabra en la lista
        if word in count_dict:      # si ya existe la clave...
            count_dict[word] += 1   # ...suma 1 al valor
        else:                       # si no existe la clave...
            count_dict[word] = 1    # ...inicializa con 1

    return count_dict


words= ["apple", "banana", "apple", "orange", "banana", "apple"]
print(word_count(words))

# En el diccionario llamado counter_dict, las key son word, los values son counter_dict[word].