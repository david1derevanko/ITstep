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
        coins = []
        listCoin = self.soup.find('tbody')
        if not listCoin:
            print("Помилка в пошуку на сторінці")
            return coins
        info = listCoin.find_all('tr')[0:10]
        for i in info:
            name = i.find('p', class_='coin-item-name')
            name2 = name.text.strip() if name else 'Відсутня назва'
            price = i.find('div', class_='sc-142c02c-0 lmjbLF')
            price2 = price.text.strip() if price else 'Відсутня ціна'
            coins.append({
                'Назва': name2,
                'Ціна': price2
            })

        return coins
    def showInfo(self, coins):
        print("\t", 'НАЗВА', '\t' * 2, 'ЦІНА')
        print('-' * 50)
        num = 1
        for i in coins:
            print(num, '\t', i['Назва'], '\t', i['Ціна'])
            num += 1

    def getTotalPrice(self, coin_name, quantity, coins):
        for coin in coins:
            if coin['Назва'] == coin_name:
                price = coin['Ціна'].replace('$', '').replace(',', '').strip()
                try:
                    price = float(price)
                    total = price * quantity
                    print(f"Загальна сума для {quantity} шт. {coin_name}: {total} ")
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
print('10 найпопулярніші криптомонети:')
if site:
    obj.showInfo(site)
    selected_coin = input("Виберіть криптовалюту для покупки (введіть назву): ")
    quantity = int(input(f"Введіть кількість криптовалюти '{selected_coin}': "))
    obj.getTotalPrice(selected_coin, quantity, site)
else:
    print("Жодної інформації не отримано")





