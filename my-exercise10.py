# Implement a function to check if a string is a palindrome.

def palindrome(string):
    mid = len(string) // 2
    first = []
    second= []
    for i in range(len(string)-1, mid, -1):
        first.append(string[i])

    for i in range(0, mid, +1):
        second.append(string[i])

    if first == second:
        return f"{string} is a palindrome"
    else:
        return f"{string} is not a palindrome"



string = "racecar"
print(palindrome(string))  # Output: "racecar is a palindrome"


#Solución alternativa:

# def palindrome(s):
#     return f"{s} is {'a' if s == s[::-1] else 'not a'} palindrome"

# print(palindrome("racecar"))  # Output: racecar is a palindrome


# ¿Qué está pasando aquí?
# s[::-1] → invierte el string.
# Comparamos s con su reverso directamente.
# Usamos una expresión condicional ('a' if ... else 'not a') para decidir el mensaje final.