import requests
from bs4 import BeautifulSoup

URL = r"https://unosmium.org/results/"
page = requests.get(URL)

DATA = "https://unosmium.org/data/{}.yaml".format

soup = BeautifulSoup(page.content, 'html.parser')

cards = soup.find_all('div', class_='card')

x = cards[0]


title = "".join(x.find("h2", class_='card-title').text.split())
print(title)

# with open("tournaments/" + title, 'w+') as fout:
link = x.find('a', href=True)['href'].split("/")
link = DATA(link[2])

with open("tournaments/" + title + ".yaml", 'w+') as fout:
    fout.write(requests.get(link).content.decode("utf-8"))
