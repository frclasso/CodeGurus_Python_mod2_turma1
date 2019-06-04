fish_tuple = (
    'catfish',
    'blowfish',
    'clowfish',
    'octopus'
)

for fish in fish_tuple:
    if fish != 'octopus':
        print(fish)

print()

for fish in fish_tuple:
    l=[]
    if fish != 'octopus':
        l.append(fish)
    print(l)

fish_list = [fish for fish in fish_tuple if fish != 'octopus']

print(fish_list)