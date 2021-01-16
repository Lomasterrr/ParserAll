import requests
from bs4 import BeautifulSoup
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
        
mailru()