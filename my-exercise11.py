# Given a list of integers, return the indices of the two numbers that add up to a specific target.

def two_num(arr, target):
    for i in arr:
        for j in arr:
            if i + j ==  target:
                return arr.index(i), arr.index(j)


arr = [2, 7, 11, 15]
target = 9
print(two_num(arr, target))  # Output: (0, 1)

#Solución alternativa:

# def two_num(arr, target):
#     seen = {}
#     for idx, num in enumerate(arr):
#         complement = target - num
#         if complement in seen:
#             return seen[complement], idx
#         seen[num] = idx

# ¿Cómo funciona esto?
# Vamos recorriendo el arreglo solo una vez.
# Para cada número, calculamos lo que le falta para llegar al target: complement = target - num.
# Si ese complemento ya lo vimos (está en el diccionario), devolvemos la tupla de índices.
# Si no, lo agregamos al diccionario con su índice.
