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
    #
    # f = open('./res.html', 'w+')
    # f.write(res.text)
    # f.close()

    soup = BeautifulSoup(res.text, 'html5lib')

    page_item = soup.find_all('li', attrs={'class': 'page-item'})

    # print(len(page_item))

    total_pages = len(page_item) - 2
    return total_pages


def get_urls():
    print('getting urls.....')

    params = {
        'page': 1
    }
    # res = session.get('http://127.0.0.1:5000', params=params)
    # soup = BeautifulSoup(res.text, 'html5lib')
    soup = BeautifulSoup(open('./res.html'), 'html5lib')


    titles = soup.find_all('h4', attrs={'class': 'card-title'})

    # menggunakna metode pengabungan url (urls = [], urls.append(url)
    urls = []

    for title in titles:
        url = title.find('a')['href']
        urls.append(url)

        print(url)

    # f = open('./res.html', 'w+')
    # f.write(res.text)
    # f.close()


def get_detail():
    print('getting detail... ')

def create_csv():
    print('csv generated... ')

def run() -> object:
    # login()
    get_urls()
    get_detail()
    create_csv()

if __name__ == '__main__':
    run()

