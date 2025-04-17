# Given a list of integers, return the longest increasing subsequence.

# def longest(arr):
#     subsec = []
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             subsec.append(arr[i: j+1])

#     valid = []
#     for num in subsec:
#         for n in num:
#             if n-1 < n:
#                 valid.append(num)

#     result = max(valid, key=len)

#     return result

# arr = [1, 2, 4, 13, 14, 16, 17, 4, 2, 5, 6, 8, 14, 19, 20]
# print(longest(arr)) # Imprimimos el arreglo de subarreglos contiguos
        

#Solucion real: la verdad no entendí cual era la definición de longest increasing subsequence.


def is_consecutive(subarr):
    subarr = sorted(set(subarr))
    if len(subarr) <= 1:
        return True
    for i in range(1, len(subarr)):
        if subarr[i] != subarr[i - 1] + 1:
            return False
    return True

def longest(arr):
    max_sub = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) + 1):
            sub = arr[i:j]
            if is_consecutive(sub) and len(sub) > len(max_sub):
                max_sub = sub
    return max_sub

arr = [1, 2, 4, 13, 14, 16, 17, 4, 2, 5, 6, 8, 14, 19, 20]
print(longest(arr))  # Output esperado: [5, 6, 8] o algo como [19, 20]


