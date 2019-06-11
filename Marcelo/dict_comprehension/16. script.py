dict1 = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5
}

dict1_comp = {k: v for (k, v) in dict1.items() if v > 2 if v % 2 == 0}

print(dict1_comp)

# tradicional
# for k, v in dict1_comp.items():
#   if v > 2:
#       if v % 2 == 0:
# print(dict1_comp.items()

doubleCondition = {k: ('par' if v % 2 == 0 else "ímpar") for (k, v) in dict1.items()}

print(doubleCondition)