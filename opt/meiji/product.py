from bs4 import BeautifulSoup
from urllib import request
import re
import time

url = 'https://www.meiji.co.jp/products/chocolate/'
response = request.urlopen(url)
soup = BeautifulSoup(response)
response.close()

choco = soup.find_all('div',attrs={'class':'l-grid-container'})
# choco = soup.find('a',attrs={'href'})
print(choco[0].text)
