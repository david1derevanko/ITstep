#import requests
#from bs4 import BeautifulSoup
#
#class Name:
#    def __init__(self,url):
#        self.url=url
#        self.header={
#            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
#
#        }
#        self.soup=None
#    def auditSite(self):
#        response= requests.get(self.url,headers=self.header)
#        if response.status_code==200:
#            self.soup=bs(response.text,"html.parser")
#        else:
#            print("Не вдалося підключитися до сайту")
#
#        def getInfo(self):
#            pass
#        def showInfo(self):
#            pass
#url="Посилання"
#obj=Name(url)
#obj.auditSite()
#site=obj.getInfo()
#if site:
#    obj.showInfo()
#else:
#    print("Жодної інформації не отримано")



#class Comfy:
#    def __init__(self,url):
#        self.url=url
#        self.header={
#            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
#
#        }
#        self.soup=None
#    def auditSite(self):
#        response= requests.get(self.url,headers=self.header)
#        if response.status_code==200:
#            self.soup=bs(response.text,"html.parser")
#        else:
#            print("Не вдалося підключитися до сайту")
#
#        def getInfo(self):
#            laptop=[]
#            lap=self.soup.find_all('div', class_='products-catalog')
#            if not lap:
#                print('Помилка в пошуку на сторінці')
#                return
#            for i in laptop[0:4]:
#                name=i.find('a', class_='prdl-item__name ellipsis-2-lines')
#                nameErorr=name.text if name else 'Відсутня назва'
#                price=i.find('div', class_='products-list-price__actions-price-current')
#                priceErorr = price.text() if price else 'Відсутня ціна'
#                laptop.apeend(
#                    {
#                        'Назва':name,
#                        'Ціна': price,
#                    }
#                )
#                return laptop
#
#        def showInfo(self):
#            print(f"\t{'НАЗВА':<}\t" * 2, f"{'ЦІНА':<}\t" * 2)
#            print("-" * 50)
#            for i in self.getInfo():
#                print(f"\t{i['Назва']}\t\t{i['Ціна']}")
#url="https://comfy.ua/ua/black-friday/cat__120/?gad_source=1&gclid=Cj0KCQiAkJO8BhCGARIsAMkswyhJ-lMrSryvvEIyf_s3FPnjgF7ydctFE_R10Yj_zj9l231aRd-ZIeAaAmjrEALw_wcB"
#obj=Comfy(url)
#obj.auditSite()
#site=obj.getInfo()
#print ("Популярні ноутбуки")
#if site:
#    obj.showInfo()
#else:
#    print("Жодної інформації не отримано")


class Comfy:
    def __init__(self,url):
        self.url=url
        self.header={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'

        }
        self.soup=None
    def auditSite(self):
        response= requests.get(self.url,headers=self.header)
        if response.status_code==200:
            self.soup=bs(response.text,"html.parser")
        else:
            print("Не вдалося підключитися до сайту")

        def getInfo(self):
            laptop=[]
            lap=self.soup.find_all('div', class_='products-catalog')
            if not lap:
                print('Помилка в пошуку на сторінці')
                return
            for i in laptop[0:4]:
                name=i.find('a', class_='prdl-item__name ellipsis-2-lines')
                nameErorr=name.text if name else 'Відсутня назва'
                price=i.find('div', class_='products-list-price__actions-price-current')
                priceErorr = price.text() if price else 'Відсутня ціна'
                laptop.apeend(
                    {
                        'Назва':name,
                        'Ціна': price,
                    }
                )
                return laptop

        def showInfo(self):
            print(f"\t{'НАЗВА':<}\t" * 2, f"{'ЦІНА':<}\t" * 2)
            print("-" * 50)
            for i in self.getInfo():
                print(f"\t{i['Назва']}\t\t{i['Ціна']}")
url="https://comfy.ua/ua/black-friday/cat__120/?gad_source=1&gclid=Cj0KCQiAkJO8BhCGARIsAMkswyhJ-lMrSryvvEIyf_s3FPnjgF7ydctFE_R10Yj_zj9l231aRd-ZIeAaAmjrEALw_wcB"
obj=Comfy(url)
obj.auditSite()
site=obj.getInfo()
print ("Популярні ноутбуки")
if site:
    obj.showInfo()
else:
    print("Жодної інформації не отримано")