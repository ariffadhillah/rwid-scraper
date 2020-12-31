import requests
from bs4 import BeautifulSoup
session = requests.Session()

def login():
    print('login...')
    datas = {
        'username': 'user',
        'password': 'user12345'
    }

    res = session.post('http://127.0.0.1:5000/login', data=datas)

    soup = BeautifulSoup(res.text, 'html5lib')

    page_item = soup.find_all('li', attrs={'class': 'page-item'})

    total_pages = len(page_item) - 2

    return total_pages


def get_urls(page):
    print('getting urls.....')

    params = {
        'page': page
    }
    res = session.get('http://127.0.0.1:5000', params=params)
    soup = BeautifulSoup(res.text, 'html5lib')



    titles = soup.find_all('h4', attrs={'class': 'card-title'})
    urls = []

    for title in titles:
        url = title.find('a')['href']
        urls.append(url)

    return urls

def get_detail():
    print('getting detail... ')

def create_csv():
    print('csv generated... ')

def run() -> object:
    total_pages = login()
    for i in range(total_pages):
        page = i + 1
        print(page)
    # get_urls()
    get_detail()
    create_csv()

if __name__ == '__main__':
    run()

