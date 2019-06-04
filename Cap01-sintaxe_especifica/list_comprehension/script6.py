kilometer = [39.2, 36.5, 37.3, 37.8]

feet = [float(3280.8399) * x for x in kilometer]
num = [x + 1 if x >= 120000 else x + 5 for x in feet]

print(num[0])

num0 ='{:.4f}'.format(num[0])
print(num0)