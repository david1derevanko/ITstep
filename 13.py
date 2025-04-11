#import requests
#from bs4 import BeautifulSoup
#
#class BooksScraper:
#    def __init__(self, url):
#        self.url = url
#        self.headers = {
#            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
#        }
#        self.soup = None
#
#    def auditSite(self):
#        response = requests.get(self.url, headers=self.headers)
#        if response.status_code == 200:
#            self.soup = BeautifulSoup(response.text, 'html.parser')
#        else:
#            print("Не вдалося підключитися до сайту")
#
#    def getInfo(self):
#        books = []
#        items = self.soup.find_all('article', class_='product_pod')[:8]
#
#        for item in items:
#            name = item.h3.a['title']
#            price = item.find('p', class_='price_color').text.strip()
#            books.append({
#                'Назва': name,
#                'Ціна': price
#            })
#        return books
#
#    def showInfo(self):
#        print(f"{'НАЗВА':<60}{'ЦІНА'}")
#        print("-" * 75)
#        for book in self.getInfo():
#            print(f"{book['Назва']:<60}{book['Ціна']}")
#
#
#url = 'http://books.toscrape.com'
#scraper = BooksScraper(url)
#scraper.auditSite()
#if scraper.soup:
#    print("Популярні книги:")
#    scraper.showInfo()
#else:
#    print("Жодної інформації не отримано")

import requests
from bs4 import BeautifulSoup

class FoxtrotScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup = None

    def auditSite(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.text, 'html.parser')
        else:
            print("Не вдалося підключитися до сайту")

    def getInfo(self):
        products = []
        cards = self.soup.find_all('div', class_='card__body')[:8]  # Перші 8 смартфонів
        for card in cards:
            name_tag = card.find('a', class_='card__title')
            price_tag = card.find('div', class_='card-price')

            name = name_tag.text.strip() if name_tag else 'Назва відсутня'
            price = price_tag.text.strip() if price_tag else 'Ціна відсутня'

            products.append({
                'Назва': name,
                'Ціна': price
            })
        return products

    def showInfo(self):
        print(f"{'НАЗВА':<70}{'ЦІНА'}")
        print("-" * 90)
        for item in self.getInfo():
            print(f"{item['Назва']:<70}{item['Ціна']}")

url = 'https://www.foxtrot.com.ua/uk/shop/smartfon.html'
scraper = FoxtrotScraper(url)
scraper.auditSite()
if scraper.soup:
    print("Популярні смартфони на Foxtrot:")
    scraper.showInfo()
else:
    print("Жодної інформації не отримано")

