dict1 = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6
}

dict1_comp = {k: v for (k,v) in dict1.items() if v > 2}
print(dict1_comp)

for k, v in dict1.items():
    if v > 2:
        print(k, ':', v)

dict2_comp = {k: v for (k, v) in dict1.items() if v > 2 if v % 2 == 0}

print(dict2_comp)

