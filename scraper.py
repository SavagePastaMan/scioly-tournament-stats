import time
import requests
import os
import logging
from bs4 import BeautifulSoup

logging.basicConfig(filename='scraper.log', level=logging.INFO)

URL = r"https://unosmium.org/results/"
page = requests.get(URL)

DATA = "https://unosmium.org/data/{}.yaml".format

soup = BeautifulSoup(page.content, 'html.parser')

cards = soup.find_all('div', class_='card')

for card in cards:
    t = card.find("h2", class_='card-title').text.split()
    title = "".join(t[:-2]).replace("/", "")
    division = "".join(t[-2:])
    link = card.find('a', href=True)['href'].split("/")
    link = DATA(link[2])

    path = os.path.join("tournaments", division, title) + '.yaml'

    if not os.path.isfile(path):
        with open(path, 'w+') as fout:
            file = requests.get(link)

            try:
                fout.write(file.content.decode('utf-8'))
            except UnicodeEncodeError as e:
                logging.warning(f"could not download {path}")
            else:
                logging.info(f"downloaded {path}")

        time.sleep(3)

