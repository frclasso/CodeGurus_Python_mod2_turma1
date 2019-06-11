import itertools

counter = itertools.count(10, 100)

# for x in counter:
#     print(x)

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

data = [100,200,300,400, 500, 600]
daily_data = list(zip(itertools.count(), data))
print(daily_data)

