import requests
from bs4 import BeautifulSoup
from time import sleep
from colorama import init
from colorama import Fore, Back, Style

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
        steamaccountall = (news.get_parser_all())
        f = open('steam_account.html', 'w')
        f.write(str(steamaccountall))


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
        mailruall = (news.get_parser_all())
        f = open('mailru_account.html', 'w')
        f.write(str(mailruall))


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
        minecraftaccountall = (news.get_parser_all())
        f = open('minecraft_account.html', 'w')
        f.write(str(minecraftaccountall))


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
        nombersall = (news.get_parser_all())
        f = open('phone_nombers.html', 'w')
        f.write(str(nombersall))


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
        yahooaccontall = (news.get_parser_all())
        f = open('yahoo_account.html', 'w')
        f.write(str(yahooaccontall))


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
        steamkeyall = (news.get_parser_all())
        f = open('steam_key.html', 'w')
        f.write(str(steamkeyall))


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
        tokendiscordall = (news.get_parser_all())
        f = open('token_discord.html', 'w')
        f.write(str(tokendiscordall))


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
        googleaccountall = (news.get_parser_all())
        f = open('google_account.html', 'w')
        f.write(str(googleaccountall))


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
        yandexall = (news.get_parser_all())
        f = open('yandex_account.html', 'w')
        f.write(str(yandexall))


def Custom():
    class AllParser:
        def __init__(self):
            self.url = 'https://yandex.ru/search/?text=host%3Apastebin.com%20' + what3 + '&lr=21329'
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
        custom = (news.get_parser_all())
        f = open('Custom.html', 'w')
        f.write(str(custom))

init(convert=True)
print(Fore.RED)
sleep(0.2)
print("     █───████─█───█─████─███─███─███─████")
sleep(0.2)
print("     █───█──█─██─██─█──█─█────█──█───█──█")
sleep(0.2)
print("     █───█──█─█─█─█─████─███──█──███─████")
sleep(0.2)
print("     █───█──█─█───█─█──█───█──█──█───█─█")
sleep(0.2)
print("     ███─████─█───█─█──█─███──█──███─█─█")

sleep(1.3)
print(Fore.LIGHTGREEN_EX)
print(" [1]List_pars, [2]Developer, [3]How it works?")
print()
what = input(" Сhoose: ")

if what == '1':
    print(Fore.RED + ' ------------------------------')
    print(Fore.LIGHTGREEN_EX + '  ▼ Here is what I can parse ▼')
    sleep(1)
    print()
    print('''  [1]Steam Accounts, [2]Steam Keys, [3]Tokens Discord,
  [4]Minecraft Accounts, [5]Google Accounts, [6]Yandex Accounts,
  [7]Yahoo Accounts, [8]Mail.ru Accounts [9]Custom''')
    print()
    what1 = input(" Сhoose: ")
print(Fore.RED + ' ------------------------------')

if what == '2':
    what1 = " by Lomaster"
    print(Fore.LIGHTMAGENTA_EX + " by Lomaster")
    print(Fore.LIGHTGREEN_EX + " Im NETSTALKER and developer python")
    print(" Country - Russia")
    print(" Telegram - @Lomasterr")
    print(Fore.RED + ' -------------------------------')

if what == '3':
    what1 = "Ты сюда не смотри, лучше уди, а то мой говнокод тебя напугает"
    print(Fore.LIGHTGREEN_EX + "   This is Yandex dorks baby.")
    print(Fore.RED + ' -------------------------------')

if what1 == '9':
    print(Fore.LIGHTGREEN_EX + ' Enter one keyword: ', end='')
    what3 = input()
    Custom()
    print(Fore.RED + ' ------------------------------')


if what1 == "1":
    steam()
    print(Fore.RED + '   All Right! Look html file.')
if what1 == "2":
    steamkey()
    print(Fore.RED + '   All Right! Look html file.')
if what1 == "3":
    tokendiscord()
    print(Fore.RED + '   All Right! Look html file.')
if what1 == "4":
    minecraftaccount()
    print(Fore.RED + '   All Right! Look html file.')
if what1 == "5":
    googleaccount()
    print(Fore.RED + '   All Right! Look html file.')
if what1 == "6":
    yandexaccount()
    print(Fore.RED + '   All Right! Look html file.')
if what1 == "7":
    yahooacconts()
    print(Fore.RED + '   All Right! Look html file.')
if what1 == "8":
    nombers()
    print(Fore.RED + '   All Right! Look html file.')
if what1 == "9":
    mailru()
    print(Fore.RED + '   All Right! Look html file.')
