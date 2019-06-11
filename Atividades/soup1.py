from bs4 import BeautifulSoup
from urllib.request import urlopen

redditFile = urlopen("http://www.reddit.com")
redditHtml = redditFile.read()

redditFile.close()

soup = BeautifulSoup(redditHtml)
redditAll = soup.find("a")
for links in soup.find_all('a'):
    print(links.get('href'))



