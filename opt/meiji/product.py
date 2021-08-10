from bs4 import BeautifulSoup
from urllib import request
import requests

import re
import time

# url = 'https://www.meiji.co.jp'
# cate = '/products/chocolate/'
# response = request.urlopen(url+cate)
# soup = BeautifulSoup(response)
# url_items = soup.select('.l-grid-row a')
# product_list =[]

# for a in url_items:
#     test = a['href']
#     eq = test.count('.html')
#     if(eq == 1):
#         url_list = url + test
#         product_list.append(url_list)

aa = requests.get('https://www.meiji.co.jp/products/chocolate/04777.html')
Beautiful = BeautifulSoup(aa.content,"html.parser")
product = Beautiful.find_all('tr')
word = [x.text.replace('\n',' ') for x in product]
print(word)
