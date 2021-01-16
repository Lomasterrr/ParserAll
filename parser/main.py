import requests
from bs4 import BeautifulSoup
from time import sleep 
print('''
 
    █── █▀▀█ █▀▄▀█ █▀▀█ █▀▀ ▀▀█▀▀ █▀▀ █▀▀█ 
    █── █──█ █─▀─█ █▄▄█ ▀▀█ ──█── █▀▀ █▄▄▀ 
    ▀▀▀ ▀▀▀▀ ▀───▀ ▀──▀ ▀▀▀ ──▀── ▀▀▀ ▀─▀▀''')
sleep(2)
print(" [1]List_pars, [2]Developer, [3]How it works?")
print()
what = input(" Сhoose: ")


if what == '1':
	print(' -----------------------------')
	print(' ▼ Here is what I can parse ▼')
	sleep(1)
	print()
	print(''' [1]Steam Accounts, [2]Steam Keys, [3]Tokens Discord,
 [4]Minecraft Accounts, [5]Google Accounts, [6]Yandex Accounts,
 [7]Yahoo Accounts, [8]Nombers Phone [9]Mail.ru Acconts''')
	print()
	print(' -----------------------------')
	what1 = input(" Сhoose: ")
sleep(100000)
class AllParser:

    def __init__(self):
        self.url = 'https://yandex.ru/search/?text=host%20%3D%20%E2%80%9Dpastebin.com%E2%80%9D%20steam%20account&lr=10716&clid=2256866-5&win=404'
        self.html = self.get_html()

    def get_html(self):
        try:
            result = requests.get(self.url)
            result.raise_for_status()
            return result.text
        except(requests.RequestException, ValueError):
            print('Server error')
            return False

    def get_parser_all(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        news_list = soup.findAll('h2', class_='organic__title-wrapper typo typo_text_l typo_line_m')
        return news_list

    
if __name__ == "__main__":
    news = AllParser()
    print(news.get_parser_all())