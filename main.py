import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import csv

f = open('quotes.csv', 'w', encoding='utf-8_sig')


for i in range(5):
    p = i + 1
    url = f'https://quotes.toscrape.com/page/{p}/'
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    quote_soup = soup.find_all('span', class_='text')
    author_soup = soup.find_all('small', class_='author')
    tag_soup = soup.find_all('a', class_='tag')
    quantity = 0
    for quote in quote_soup:
        quantity += 1
        f.write(f'Page {p}, tag of this post: {tag_soup[quantity-1].text},'
                f' Quote {quantity} by {author_soup[quantity-1].text} : ' + quote.text + '\n')
    sleep(1)

f.close()




