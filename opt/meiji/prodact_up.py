import random
import string
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
from bs4 import BeautifulSoup
from urllib import request
import requests

choco_brand_list = ['','ミルクチョコレート','明治 ザ・チョコレート','アーモンドチョコレート','マカダミアチョコレート','その他ナッツチョコレート','きのこの山','たけのこの里','きのこの山とたけのこの里','チョコレート効果','オリゴスマート','明治TANPACT','エムズバー','ガルボ','フラン','ホルン','プッカ','アグロフォレストリーミルクチョコレート','MyチョコBox','小粒チョコ','リッチチョコサンド']
cate_last = ['チョコレート','（準）チョコレート','チョコレート菓子','（準）チョコレート菓子','菓子詰合せ']

# Use a service account
cred = credentials.Certificate('../umyfoods-rac-firebase-adminsdk-m6vos-476571680f.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
dt_now = datetime.datetime.now()

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

        # id作成
        dat = string.digits + string.ascii_lowercase + string.ascii_uppercase
        rand = ''.join([random.choice(dat) for i in range(19)])

        # ブランド
        for hit in Beautiful.find_all(attrs={'class':'m-heading1'}):
            brand = hit.contents[0].text
        
        l_start = [s for s in choco_brand_list if s.startswith(brand)]

        # 商品名
        for hit in Beautiful.find_all(attrs={'class':'m-heading1'}):
            name = hit.contents[1]

        # 商品概要
        # product = Beautiful.find_all('tr')
        # word = [x.text.replace('\n',' ') for x in product]

        # 栄養成分
        Nutritional_subject = Beautiful.find_all('h2')
        Nutritional_ingredients_subject = [x.text.replace('\n',' ') for x in Nutritional_subject]

        # 名前
        Nutritional_name = Beautiful.find_all('th')
        Nutritional_ingredients_name = [x.text.replace('\n',' ') for x in Nutritional_name]
        
        # 数値
        Nutritional_value = Beautiful.find_all('td')
        Nutritional_ingredients_value = [x.text.replace('\n',' ') for x in Nutritional_value]

        # eiyou_len = len(Nutritional_ingredients_name)-4

        category_mix = '00' + str(cate_last.index(Nutritional_ingredients_value[0]))

        category_a = int(category_mix)+1

        doc_ref = db.collection(u'product').document(rand)
        doc_ref.set({
            u'add_date': dt_now,
            # u'allergy_id': ['006'],
            u'brand_id': str(choco_brand_list.index(brand)),
            u'category_id': ['001','004','00'+str(category_a)],
            u'maker_id':'02zzgbAq1OxeXVMxoEhq',
            u'product_id': rand,
            u'product_name': name,
            u'raw_material': Nutritional_ingredients_value[1],
            u'update_date': dt_now
        })
        doc_ref.collection(u'nutritional_ingredients').document(rand).set({
            Nutritional_ingredients_name[4]:Nutritional_ingredients_value[4],
            Nutritional_ingredients_name[5]:Nutritional_ingredients_value[5],
            Nutritional_ingredients_name[6]:Nutritional_ingredients_value[6],
            Nutritional_ingredients_name[7]:Nutritional_ingredients_value[7],
            Nutritional_ingredients_name[8]:Nutritional_ingredients_value[8],
            u'subject':Nutritional_ingredients_subject[1]
        })