import requests
from bs4 import BeautifulSoup
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

