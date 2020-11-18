import requests
from bs4 import BeautifulSoup

URL = r"https://unosmium.org/results/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='all')
