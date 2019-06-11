dict1 = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6
}

# dict1_comp = {k:v for(k, v) in dict1.items() if v > 2 if v % 2 == 0 if v % 3 == 0}
dict1_comp = {k:v for(k, v) in dict1.items() if v > 2 if v % 2 == 0}
print (dict1_comp)

# tradicional
# for k, v in dict1_comp.items():
#     if v > 2 :
#         if v % 2 == 0:
#             if v % 3 == 0:
#                 print(k,":", v)

doubleCondition = {k:('par' if v % 2 == 0 else 'impar') for(k,v) in dict1.items()}
print(doubleCondition)