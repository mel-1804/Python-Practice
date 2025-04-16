# Write a function that returns the first non-repeating character in a string. If none exists, return None.

def new_funct(string):
    aux = {}
    for i in string:
        if i in aux:
            aux[i] += 1
        else:
            aux[i] = 1

    first_one = None
    for i in string:
        if aux[i] == 1:
            first_one = i
            break
    
    return first_one


string = "swiss"
print(f"the first element without repeating is: {new_funct(string)}")  # Output: "w


#alternative solution:
# def first_unique_char(s):
#     from collections import Counter
#     counts = Counter(s)
#     return next((char for char in s if counts[char] == 1), None)

# print(f"the first element without repeating is: {first_unique_char('swiss')}")




        