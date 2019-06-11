# https://currencylayer.com

import json #dicionário
from urllib.request import urlopen


with urlopen("http://www.apilayer.net/api"
             "/live?access_key=19b97a033fd712c7aca6d6060f44fbbe&format=1") as response:
    source = response.read()

data = json.loads(source)
print(data)
print(type(data))


print()

print(json.dumps(data, indent=2))