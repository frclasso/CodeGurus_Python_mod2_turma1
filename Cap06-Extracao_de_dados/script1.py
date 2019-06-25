
#!/usr/bin/env python3

# web scraping com BeautifulSoup
import requests
from bs4 import BeautifulSoup

# 1) Coletar a primeira pagina da lista de artistas
page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')

# 2) Criar o objeto BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')


#6) remover links inferiores
last_links = soup.find(class_="AlphaNav")
last_links.decompose()

# 3) Pegar todo o texto da div BodyText
artist_name_list = soup.find(class_='BodyText')

# 4) Pegar o texto de todas as instancias da tag <a> dentro da div BodyText
artist_name_list_items = artist_name_list.find_all('a')



# 5) Criar loop para imprimir todos os nomes de artistas
# for artist_name in artist_name_list_items:
#     print(artist_name.prettify())

#7) nomes
for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    links = 'https://web.archive.org/' + artist_name.get('href')  # 8) links dos artistas
    print(names)
    print(links)
