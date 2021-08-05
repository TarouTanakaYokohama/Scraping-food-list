from bs4 import BeautifulSoup
from urllib import request

import re
import time

url = 'https://www.meiji.co.jp'
cate = '/products/chocolate/'
response = request.urlopen(url+cate)
soup = BeautifulSoup(response)
product_list =[]

url_items = soup.select('.l-grid-row a')

for a in url_items:
    test = a['href']
    eq = test.count('.html')
    if(eq == 1):
        url_list = url + test
        product_list.append(url_list)

