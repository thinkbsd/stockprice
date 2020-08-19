import requests
from bs4 import BeautifulSoup

page = requests.get('https://finance.yahoo.com/quote/GOOG?ltr=1')
soup = BeautifulSoup(page.content, 'html.parser')
container = soup.select_one('div#quote-header-info')

print(container.find('h1').text)

for ele in container.find_all('span'):
    print(ele.text)