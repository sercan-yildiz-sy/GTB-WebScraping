import requests
import json
from bs4 import BeautifulSoup

# This script scrapes the Istanbul University newspaper archive using BeautifulSoup and saves the dates and URLs of newspapers in a JSON file.

# The main page is fetched and parsed to find newspaper names and their URLs.
main_page = requests.get('https://nek.istanbul.edu.tr/ekos/GAZETE/').text
soup = BeautifulSoup(main_page, 'html.parser')

# Extracting newspaper names
newspapers = []
for names in soup.find_all('span', class_='caption mb-2 d-block'):
    newspapers.append(names.get_text(strip = True))

# Extracting newspaper URLs
links = []
for link in soup.find_all('a'):
    li = link.get('href')
    if li[0] == "g":
        links.append(li)

newspapersDict = {}
# The script iterates through the list of newspapers and scrapes each newspaper's page for dates and URLs and saves them in a dictionary.
for i in range(len(newspapers)):
    newspaperPage = requests.get('https://nek.istanbul.edu.tr/ekos/GAZETE/' + links[i]).text
    soup2 = BeautifulSoup(newspaperPage, 'html.parser')
    dates = []
    urls = []
    for date in soup2.find_all('td', class_='tm-text-left'):
        dates.append(date.get_text(strip = True))

    for url in soup2.find_all('a', href=True):
        if url['href'].endswith('.pdf'):
            urls.append(url['href'])

    newspapersDict[newspapers[i]] = list(zip(dates, urls))

# The JSON file is created and saved with the newspaper names as keys and a list of tuples (date, URL) as values.
with open('newspapers_bs4.json', 'w', encoding='utf-8') as f:
    json.dump(newspapersDict, f, ensure_ascii=False, indent=2)