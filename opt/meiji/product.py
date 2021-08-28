from bs4 import BeautifulSoup
from urllib import request
import requests
import time
import random
import string
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

url = 'https://www.meiji.co.jp'
cate = '/products/chocolate/'
response = request.urlopen(url+cate)
soup = BeautifulSoup(response)
url_items = soup.select('.l-grid-row a')
product_list =[]

for a in url_items:
    test = a['href']
    eq = test.count('.html')
    if(eq == 1):
        url_list = url + test
        product_list.append(url_list)
        aa = requests.get(url_list)
        Beautiful = BeautifulSoup(aa.content,"html.parser")
        product = Beautiful.find_all('td')
        word = [x.text.replace('\n',' ') for x in product]

        print(word[1])
        time.sleep(2)

# Use a service account
cred = credentials.Certificate('umyfoods-rac-firebase-adminsdk-m6vos-476571680f.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# 現時刻取得
dt_now = datetime.datetime.now()

# id作成
dat = string.digits + string.ascii_lowercase + string.ascii_uppercase
rand = ''.join([random.choice(dat) for i in range(19)])

# firestoreに追加
doc_ref = db.collection(u'product').document(rand)
doc_ref.set({
    u'add_date': dt_now,
    u'allergy_id': ['006'],
    u'brand_id': u'003',
    u'category_id': ['001','007','001'],
    u'maker_id':'001',
    u'product_id': rand,
    u'product_name': u'午後の紅茶',
    u'raw_material': u'水,小茶,乳',
    u'update_date': dt_now
})