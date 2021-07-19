from bs4 import BeautifulSoup
from urllib import request
import re

url = 'https://www.meiji.co.jp/products/chocolate/'
response = request.urlopen(url)
soup = BeautifulSoup(response)
response.close()

choco = soup.find_all('p',attrs={'class':'m-anchorLink-block'}) 
print(choco)
