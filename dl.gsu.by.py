import requests
from bs4 import BeautifulSoup as Bs

login = ['login', 'password']
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.65'}
payload = {'id': login[0],
           'password': login[1],
           'lng': 'ru',
           'logon': 'submit'
           }
url = 'https://dl.gsu.by/login.jsp'
session = requests.Session()
session.headers.update(headers)
responce = session.post(url, data=payload)
soup = Bs(responce.text, 'lxml')
payload['id'] = soup.find('input').get('value')
url = 'https://dl.gsu.by/logon.asp'
session.post(url, data=payload)
responce = session.get('The link you want to get HTML-code from')
responce.encoding = 'windows-1251'
with open(r'path', 'w') as file:
    file.write(responce.text)
