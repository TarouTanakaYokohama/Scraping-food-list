from bs4 import BeautifulSoup
from urllib import request
import re
import time

url = 'https://www.meiji.co.jp'
cate = '/products/chocolate/'
response = request.urlopen(url+cate)
soup = BeautifulSoup(response)

# choco = soup.find_all('ul', attrs={'class': 'l-grid-row'})
# url = soup.find_all('a', attrs={'class': 'l-card'})

url_items = soup.select('.l-grid-row a')

for a in url_items:
    print(url+a['href'])
