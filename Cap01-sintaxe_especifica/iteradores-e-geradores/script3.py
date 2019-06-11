import itertools

def get_state(person):
    return person['state']

people =[
    {
        'name':'John Doe',
        'city':'Gothan',
        'state':'NY'
    },
    {
        'name':'Corey Shaefer',
        'city':'Boulder',
        'state':'CO'
    },
    {
        'name':'Albert Einstein',
        'city':'Denver',
        'state':'CO'
    },
    {
        'name':'John Henry',
        'city':'Hilton',
        'state':'WV'
    },
    {
        'name':'Randy Moss',
        'city':'Rand',
        'state':'WV'
    },
    {
        'name':'Nicole K',
        'city':'Asheville',
        'state':'NC'
    },
    {
        'name':'Jame Taylor',
        'city':'Oklahoma',
        'state':'OH'
    },
{
        'name':'Jame Taylor',
        'city':'New ',
        'state':'NY'
    },
]
person_group = itertools.groupby(people, get_state)
for state, group in person_group:
    #print(k, v)
    # for person in v:
    #     print(person)
    print(state, len(list(group)))