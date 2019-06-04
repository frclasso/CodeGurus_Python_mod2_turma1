list_of_list = [
    [1,2,3],[4,5,6],[7,8,9]
]

listaUnica = [y for x in list_of_list for y in x]
print(listaUnica)


# listaUnica2 = []
# for x in list_of_list:
#     for y in x:
#         listaUnica2.append(y)
#
# print(listaUnica2)