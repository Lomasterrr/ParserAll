import requests
from bs4 import BeautifulSoup
from time import sleep 

def steam():
    class AllParser:
        def __init__(self):
            self.url = 'https://yandex.ru/search/?text=host%3Apastebin.com%20SteamAccounts&lr=10716&clid=2256866-5&win=404'
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
        
def mailru():
    class AllParser:
        def __init__(self):
            self.url = 'https://yandex.ru/search/?lr=10716&text=host%3Apastebin.com%20mail.ru%20account'
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
        
def minecraftaccount():
    class AllParser:
        def __init__(self):
            self.url = 'https://yandex.ru/search/?text=host%3Apastebin.com%20minecraft%20account&lr=10716&clid=2256866-5&win=404'
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

def nombers():
    class AllParser:
        def __init__(self):
            self.url = 'https://yandex.ru/search/?text=host%3Apastebin.com%20nomber%20phone&lr=10716&clid=2256866-5&win=404'
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
        
def yahooacconts():
    class AllParser:
        def __init__(self):
            self.url = 'https://yandex.ru/search/?text=host%3Apastebin.com%20yahoo%20acconts&lr=10716&clid=2256866-5&win=404'
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
        
def steamkey():
    class AllParser:
        def __init__(self):
            self.url = 'https://yandex.ru/search/?text=host%3Apastebin.com%20Steam%20Key&lr=10716&clid=2256866-5&win=404'
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
        
def tokendiscord():
    class AllParser:
        def __init__(self):
            self.url = 'https://yandex.ru/search/?text=host%3Apastebin.com%20token%20discord&lr=10716&clid=2256866-5&win=404'
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

def googleaccount():
    class AllParser:
        def __init__(self):
            self.url = 'https://yandex.ru/search/touch/?text=host%3Apastebin.com%20%40gmail.com%20pass%20&lr=10716&clid=2256866-5&win=404'
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
        
def yandexaccount():
    class AllParser:
        def __init__(self):
            self.url = 'https://yandex.ru/search/touch/?text=host%3Apastebin.com%20%40yandex.ru%20pass%20&lr=10716&clid=2256866-5&win=404'
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

       
        
print('''
     █───████─█───█─████─███─███─███─████
     █───█──█─██─██─█──█─█────█──█───█──█
     █───█──█─█─█─█─████─███──█──███─████
     █───█──█─█───█─█──█───█──█──█───█─█
     ███─████─█───█─█──█─███──█──███─█─█''')
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
 [7]Yahoo Accounts, [8]Nombers Phone [9]Mail.ru Accounts''')
	print()
        print(' -----------------------------')
	what1 = input(" Сhoose: ")

if what == '2':
    what1 = " by Lomaster"
    print(what1)
    print(" Im NETSTALKER and developer python")
    print(" Country - Russia")
    print(" Telegram - @Lomasterr")
    print(' -----------------------------')

if what == '3':
	what1 = "Ты сюда не смотри лучше уди, а то мой говнокод тебя напугает"
	print(" This is Yandex dorks baby")
	print(' -----------------------------')
    
	

if what1 == "1":
	 steam()
	 
elif what1 == "2":
	 steamkey()
	 
elif what1 == "3":
	 tokendiscord()
	 
elif what1 == "4":
	minecraftaccount()

elif what1 == "5":
	googleaccount()

elif what1 == "6":
	yandexaccount()
	
elif what1 == "7":
	yahooacconts()

elif what1 == "8":
	nombers()
	
elif what1 == "9":
	mailru()

