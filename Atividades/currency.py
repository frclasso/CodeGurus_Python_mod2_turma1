

#https://currencylayer.com


import json
from urllib.request import urlopen

with urlopen("http://www.apilayer.net/api"
             "/live?access_key=19b97a033fd712c7aca6d6060f44fbbe&format=1") as response:
    source = response.read()
    
data = json.loads(source)
# print(data)
# print(type(data))

print(json.dumps(data, indent=2))

usd_rates = dict()
for moedas, valores in data['quotes'].items():
    usd_rates[moedas] = valores
#print(usd_rates)
print("Convertendo Dolar para Real: {}".format(usd_rates['USDBRL']))
print("Convertendo Dolar para Euro: {}".format(usd_rates['USDEUR']))
print("Convertendo Dolar para Peso Argentino: {}".format(usd_rates['USDARS']))
print("Convertendo Dolar para Dolar Australiano: {}".format(usd_rates['USDAUD']))
print("Convertendo Dolar para Dolar Canadense: {}".format(usd_rates['USDCAD']))