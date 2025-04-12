import requests
from bs4 import BeautifulSoup as bs

class Coin:
    def __init__(self, url):
        self.url = url
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup = None
    def auditSite(self):
        response = requests.get(self.url, headers=self.header)
        if response.status_code == 200:
            self.soup = bs(response.text, "html.parser")
        else:
            print("Не вдалося підключитися до сайту")
    def getInfo(self):
        NFTs = []
        listNFTs = self.soup.find('tbody')
        if not listNFTs:
            print("Помилка в пошуку на сторінці")
            return NFTs
        info = listNFTs.find_all('tr')[0:10]
        for i in info:
            name = i.find('div', class_='NFTCollectionListPage_collection-name__cKjig')
            name2 = name.text.strip() if name else 'Відсутня назва'
            price = i.find('div', class_='sc-65e7f566-0 cMQTbZ')
            price2 = price.text.strip() if price else 'Відсутня ціна'
            NFTs.append({
                'Назва': name2,
                'Ціна': price2
            })

        return NFTs
    def showInfo(self, NFTs):
        print("\t", 'НАЗВА', '\t' * 2, 'ЦІНА')
        print('-' * 50)
        num = 1
        for i in NFTs:
            print(num, '\t', i['Назва'], '\t', i['Ціна'])
            num += 1

    def getTotalPrice(self, NFTs_name, quantity, NFTs):
        for NFTs in NFTs:
            if NFTs['Назва'] == NFTs_name:
                price = NFTs['Ціна'].replace('$', '').replace(',', '').strip()
                try:
                    price = float(price)
                    total = price * quantity
                    print(f"Загальна сума для {quantity} шт. {NFTs_name}: {total} ")
                    return total
                except ValueError:
                    print("Невірна ціна для обчислення.")
                    return 0
        print("Товар не знайдено в списку.")
        return 0
url = "https://coinmarketcap.com/"
obj = Coin(url)
obj.auditSite()
site = obj.getInfo()
print('10 найпопулярніші NFTs:')
if site:
    obj.showInfo(site)
    selected_NFTs = input("Виберіть NFTs для покупки (введіть назву): ")
    quantity = int(input(f"Введіть кількість NFTs '{selected_NFTs}': "))
    obj.getTotalPrice(selected_NFTs, quantity, site)
else:
    print("Жодної інформації не отримано")