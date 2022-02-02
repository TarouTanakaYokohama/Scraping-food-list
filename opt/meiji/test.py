import random
import string
from typing import Counter
from unicodedata import category
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
from bs4 import BeautifulSoup
from urllib import request
import spacy
import ginza

Allergie = []

# Use a service account
cred = credentials.Certificate(
    '../umyfoods-rac-firebase-adminsdk-m6vos-476571680f.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
dt_now = datetime.datetime.now()

dat = string.digits + string.ascii_lowercase + string.ascii_uppercase
rand = ''.join([random.choice(dat) for i in range(19)])

url = 'https://www.meiji.co.jp'
cate = '/products/chocolate/'
response = request.urlopen(url+cate)
soup = BeautifulSoup(response)
url_items = soup.select('.l-grid-row a')


major_category = '001'
categorys = '001'
sub_category = '005'

Internal_capacity = ""
# Morphological_analysis = ['']
maker_id = "7XGZ6bWYbHlp0JgQlz5"
brand_id = "1"
maker_url = "https://www.yagai.net/commodity/salami-calpas/44/"
product_name = "おやつカルパスカレー味"
raw_material = "鶏肉（国産）、豚脂肪、結着材料（粗ゼラチン、でん粉）、豚肉、糖類（麦芽糖、砂糖）、食塩、香辛料、豚コラーゲン／調味料（アミノ酸）、リン酸塩（Na，K）、pH調整剤、酸化防止剤（V. C）、くん液、保存料（ソルビン酸K）、発色剤（亜硝酸Na）、（一部に鶏肉・豚肉・ゼラチンを含む）"
subject = "	1本（3g）当たり"
Nutritional_ingredients_dick = {'たんぱく質':'0.7g','エネルギー':'14kcal','炭水化物':'0.3g','脂質':'1.1g','食塩相当量':'0.1g'}

images = [""]


allergy_list = []

simple_name_strip = product_name

nlp = spacy.load('ja_ginza')  # モデルのロード
doc = nlp(product_name)
Morphological_analysis = []

allergy_list = []

for i in range(28):
    i +=1
    if i <10:
        Allergie.append('00'+str(i))
    else :
        Allergie.append('0'+str(i))

if any(map(raw_material.__contains__, ("えび", "海老", "エビ"))):
    allergy_list.append(Allergie[0])
if any(map(raw_material.__contains__, ("かに", "蟹", "カニ", "ガニ", "がに"))):
    allergy_list.append(Allergie[1])
if any(map(raw_material.__contains__, ("小麦", "こむぎ", "コムギ"))):
    allergy_list.append(Allergie[2])
if any(map(raw_material.__contains__, ("そば", "ソバ"))):
    allergy_list.append(Allergie[3])
if any(map(raw_material.__contains__, ("卵","玉子","たまご","タマゴ","エッグ","鶏卵","あひる卵","うずら卵"))):
    allergy_list.append(Allergie[4])
    if any(map(raw_material.__contains__, ("魚卵","爬虫類卵","昆虫卵"))):
        allergy_list.pop()
if any(map(raw_material.__contains__, ("乳","ミルク","バター","バターオイル","チーズ","アイスクリーム"))):
    allergy_list.append(Allergie[5])
    if any(map(raw_material.__contains__, ("乳酸","乳酸菌","生山羊乳","生めん羊乳","殺菌山羊乳"))):
        allergy_list.pop()
if any(map(raw_material.__contains__, ("落花生", "ピーナッツ","なんきんまめ"))):
    allergy_list.append(Allergie[6])
if any(map(raw_material.__contains__, ("アーモンド", "あーもんど"))):
    allergy_list.append(Allergie[7])
if any(map(raw_material.__contains__, ("あわび", "アワビ"))):
    allergy_list.append(Allergie[8])
    if any(map(raw_material.__contains__, ("チリアワビ","ちりあわび"))):
        allergy_list.pop()
if any(map(raw_material.__contains__, ("いか", "イカ"))):
    allergy_list.append(Allergie[9])
if any(map(raw_material.__contains__, ("いくら", "イクラ", "すじこ", "スジコ"))):
    allergy_list.append(Allergie[10])
if any(map(raw_material.__contains__, ("オレンジ", "おれんじ"))):
    allergy_list.append(Allergie[11])
if any(map(raw_material.__contains__, ("カシューナッツ", "かしゅーなっつ"))):
    allergy_list.append(Allergie[12])
if any(map(raw_material.__contains__, ("キウイフルーツ", "キウイ", "キウィー", "キーウィー", "キーウィ", "キウィ"))):
    allergy_list.append(Allergie[13])
if any(map(raw_material.__contains__, ("牛肉","牛", "ビーフ", "ぎゅうにく", "ぎゅう肉", "牛にく","ラード","ヘッド"))):
    allergy_list.append(Allergie[14])
if any(map(raw_material.__contains__, ("くるみ", "クルミ"))):
    allergy_list.append(Allergie[15])
if any(map(raw_material.__contains__, ("ごま", 'ゴマ', '胡麻'))):
    allergy_list.append(Allergie[16])
    if any(map(raw_material.__contains__, ("トウゴマ","唐胡麻","エゴマ","荏胡麻"))):
        allergy_list.pop()
if any(map(raw_material.__contains__, ("さけ", "鮭", "サケ", "サーモン", "しゃけ", "シャケ"))):
    allergy_list.append(Allergie[17])
if any(map(raw_material.__contains__, ("さば", "鯖", "サバ"))):
    allergy_list.append(Allergie[18])
if any(map(raw_material.__contains__, ("大豆", "だいず", "ダイズ","枝豆"))):
    allergy_list.append(Allergie[19])
if any(map(raw_material.__contains__, ("鶏肉","とりにく","とり肉","鳥肉","鶏","鳥","とり","チキン","どり","ドリ"))):
    allergy_list.append(Allergie[20])
    if any(map(raw_material.__contains__, ("鶏卵","けいらん"))):
        allergy_list.pop()
if any(map(raw_material.__contains__, ("バナナ", "ばなな"))):
    allergy_list.append(Allergie[21])
if any(map(raw_material.__contains__, ("豚肉","ぶたにく","豚にく","ぶた肉","豚","ポーク"))):
    allergy_list.append(Allergie[22])
if any(map(raw_material.__contains__, ("まつたけ", "松茸", "マツタケ"))):
    allergy_list.append(Allergie[23])
if any(map(raw_material.__contains__, ("もも", "モモ", "桃", "ピーチ"))):
    allergy_list.append(Allergie[24])
if any(map(raw_material.__contains__, ("やまいも", "山芋", "ヤマイモ", "山いも"))):
    allergy_list.append(Allergie[25])
if any(map(raw_material.__contains__, ("りんご", "リンゴ", "アップル"))):
    allergy_list.append(Allergie[26])
if any(map(raw_material.__contains__, ("ゼラチン", "ぜらちん"))):
    allergy_list.append(Allergie[27])

for sent in doc.sents:
    for i, token in enumerate(sent):
            Morphological_analysis.append(token.orth_)
if len(Morphological_analysis) != 1 and len(Morphological_analysis) != 0:
    for i in range(len(Morphological_analysis)):
        Morphological_analysis.append(
            Morphological_analysis[i]+Morphological_analysis[i+1])
    Morphological_analysis.pop()
if len(Morphological_analysis) == 1:
    Morphological_analysis.pop()
Morphological_analysis.append(simple_name_strip)

if not allergy_list:
    allergy_list.append('')

doc_ref = db.collection(u'product').document('0'+rand)
doc_ref.set({
    u'add_date': dt_now,
    u'allergy_id': allergy_list,
    u'brand_id': brand_id,
    u'category_id': [major_category, categorys, sub_category],
    u'maker_id': maker_id,
    u'product_id': '0'+rand,
    u'product_name': product_name,
    u'raw_material': raw_material,
    u'Internal_capacity': Internal_capacity,
    u'update_date': dt_now,
    u'images': images,
    u'release_date': datetime.datetime(1, 1, 1, 1, 1, 1, 1),
    u'maker_url': maker_url,
    u'delete_flag': False,
    u'delete_date': dt_now,
    u'Morphological_analysis': Morphological_analysis
})
doc_ref.collection(u'nutritional_ingredients').document('0'+rand).set({
    u'Nutritional_ingredients': Nutritional_ingredients_dick,
    u'subject': subject
})