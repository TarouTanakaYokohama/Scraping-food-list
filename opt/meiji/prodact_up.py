import random
import string
from typing import Counter
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
from bs4 import BeautifulSoup
from urllib import request
import requests
import re
# 形態素解析
# from janome.tokenizer import Tokenizer
import spacy
import ginza

# n-gram関数


def n_gram(target, n):
    # 基準を1文字(単語)ずつ ずらしながらn文字分抜き出す
    return [target[idx:idx + n] for idx in range(len(target) - n + 1)]


choco_brand_list = ['', 'ミルクチョコレート', '明治 ザ・チョコレート', 'アーモンドチョコレート', 'マカダミアチョコレート', 'その他ナッツチョコレート', 'きのこの山', 'たけのこの里', 'きのこの山とたけのこの里',
                    'チョコレート効果', 'オリゴスマート', '明治TANPACT', 'メルティーキッス', 'ガルボ', 'フラン', 'ホルン', 'プッカ', 'アグロフォレストリーミルクチョコレート', 'MyチョコBox', '小粒チョコ', 'リッチチョコサンド']
cate_last = ['チョコレート', '（準）チョコレート', 'チョコレート菓子', '（準）チョコレート菓子', '菓子詰合せ']

Allergie = []
for i in range(28):
    i +=1
    if i <10:
        Allergie.append('00'+str(i))
    else :
        Allergie.append('0'+str(i))

# Use a service account
# cred = credentials.Certificate(
#     '../umyfoods-rac-firebase-adminsdk-m6vos-476571680f.json')

# firebase_admin.initialize_app(cred)

# db = firestore.client()
# dt_now = datetime.datetime.now()

url = 'https://www.meiji.co.jp'
cate = '/products/chocolate/'
response = request.urlopen(url+cate)
soup = BeautifulSoup(response)
url_items = soup.select('.l-grid-row a')
product_list = []


# nlp = spacy.load('ja_ginza_electra')  # モデルのロード
nlp = spacy.load('ja_ginza')  # モデルのロード

for a in url_items:
    test = a['href']
    eq = test.count('.html')
    if(eq == 1):
        url_list = url + test
        product_list.append(url_list)

        aa = requests.get(url_list)
        Beautiful = BeautifulSoup(aa.content, "html.parser")

        # id作成
        dat = string.digits + string.ascii_lowercase + string.ascii_uppercase
        rand = ''.join([random.choice(dat) for i in range(19)])

        # ブランド
        for hit in Beautiful.find_all(attrs={'class': 'm-heading1'}):
            brand = hit.contents[0].text

        l_start = [s for s in choco_brand_list if s.startswith(brand)]

        # 商品名
        for hit in Beautiful.find_all(attrs={'class': 'm-heading1'}):
            name = hit.contents[1]
        aiu = re.findall('.* ', name)
        simple_name = "".join(map(str, aiu))
        simple_name_strip = simple_name.strip()

        # 商品概要
        # product = Beautiful.find_all('tr')
        # word = [x.text.replace('\n',' ') for x in product]

        # 栄養成分
        Nutritional_subject = Beautiful.find_all('h2')
        Nutritional_ingredients_subject = [
            x.text.replace('\n', ' ') for x in Nutritional_subject]

        Nutritional_ingredients_subject_list = []
        for i, s in enumerate(Nutritional_ingredients_subject[1].split()):
            if i != 0:
                Nutritional_ingredients_subject_list.append(s)
        Nutritional_ingredients_subject_text = (
            ' '.join(Nutritional_ingredients_subject_list))

        # リスト
        Nutritional_ingredients_dick = {}
        Nutritional_name_list = []
        Nutritional_value_list = []
        Nutritional_name = Beautiful.find_all('th')
        Nutritional_value = Beautiful.find_all('td')

        num = 0

        Nutritional_ingredients_name = [
            x.text.replace('\n', ' ') for x in Nutritional_name]

        for Nutritional_ingredients_count in range(len(Nutritional_ingredients_name)):
            True

        for i, s in enumerate(Nutritional_name):
            # 名前
            Nutritional_ingredients_name = [
                x.text.replace('\n', ' ') for x in Nutritional_name]
            # 数値
            Nutritional_ingredients_value = [
                x.text.replace('\n', ' ') for x in Nutritional_value]

            if Nutritional_ingredients_name[i] in "名称":
                Nutritional_name_list.append(Nutritional_ingredients_name[i])
                Nutritional_value_list.append(Nutritional_ingredients_value[i])
            if Nutritional_ingredients_name[i] in "原材料名":
                Nutritional_name_list.append(Nutritional_ingredients_name[i])
                Nutritional_value_list.append(Nutritional_ingredients_value[i])
            if Nutritional_ingredients_name[i] in "内容量":
                Nutritional_name_list.append(Nutritional_ingredients_name[i])
                Nutritional_value_list.append(Nutritional_ingredients_value[i])
            if Nutritional_ingredients_name[i] in "エネルギー":
                num = i

        # 栄養成分の処理
        for i in enumerate(range(len(Nutritional_name)-num)):
            Nutritional_ingredients_dick |= {
                Nutritional_ingredients_name[num+i[0]]: Nutritional_ingredients_value[num+i[0]]}

        category_mix = '00' + \
            str(cate_last.index(Nutritional_value_list[0]))

        category_a = int(category_mix)+1

        # 商品名の空白を削除
        product_split = simple_name.replace(' ', '')
        # 商品名を２文字ずつ区切る
        # gram = n_gram(product_split,2)
        # print(gram)
        # 商品名を形態素解析
        # Janomeバージョン
        # t_wakati = Tokenizer(wakati=True)
        # Morphological_analysis = list(t_wakati.tokenize(product_split))
        # print(Morphological_analysis)

        # ginzaバージョン
        doc = nlp(product_split)
        Morphological_analysis = []

        for sent in doc.sents:
            for i, token in enumerate(sent):
                if token.pos_ in ('NOUN', 'PRON', 'PROPN', 'VERB', 'ADJ'):
                    Morphological_analysis.append(token.orth_)
                # if token.orth_ == '％' or token.orth_ == '袋':
                if token.orth_ == '％':
                    Morphological_analysis.pop()
        for i in range(len(Morphological_analysis)):
            Morphological_analysis.append(
                Morphological_analysis[i]+Morphological_analysis[i+1])

        Morphological_analysis.pop()
        Morphological_analysis.append(simple_name_strip)
        print(Morphological_analysis)

        # 原材料からアレルギーを取得
        allergy_list = []

        if any(map(Nutritional_ingredients_value[1].__contains__, ("えび", "海老", "エビ"))):
            allergy_list.append(Allergie[0])
        if any(map(Nutritional_ingredients_value[1].__contains__, ("かに", "蟹", "カニ", "ガニ", "がに"))):
            allergy_list.append(Allergie[1])
        if any(map(Nutritional_ingredients_value[1].__contains__, ("小麦", "こむぎ", "コムギ", "パン", "うどん", 'デュラムセモリナ'))):
            allergy_list.append(Allergie[2])
        if any(map(Nutritional_ingredients_value[1].__contains__, ("そば", "ソバ"))):
            allergy_list.append(Allergie[3])
        if any(map(Nutritional_ingredients_value[1].__contains__, ("卵白", "卵黄", "玉子", "たまご", "タマゴ", "エッグ", "鶏卵", "あひる卵", "うずら卵", "マヨネーズ", "オムレツ", "目玉焼", "かに玉", "オムライス", "親子丼", '卵殻カルシウム'))):
            allergy_list.append(Allergie[4])
        if any(map(Nutritional_ingredients_value[1].__contains__, ("生乳", "牛乳", "特別牛乳", "成分調整牛乳""低脂肪牛乳", "無脂肪牛乳", "加工乳", "乳製品", "バター", "バターオイル", "チーズ", "濃縮ホエイ", "アイスクリーム", "濃縮乳", "脱脂濃縮乳", "無糖れん乳", "無糖練乳", "無糖脱脂れん乳", "無糖脱脂練乳", "加糖れん乳", "加糖練乳", "加糖脱脂れん乳", "加糖脱脂練乳", "全粉乳", "脱脂粉乳", "たんぱく質濃縮", "バターミルクパウダー", "加糖粉乳", "調製粉乳", "発酵乳", "はっ酵乳", "乳酸菌飲料", "乳飲料", "カゼイン", "生クリーム", "ヨーグルト", "アイスミルク", "ラクトアイス", "ミルク", "乳成分"))):
            allergy_list.append(Allergie[5])
        if any(map(Nutritional_ingredients_value[1].__contains__, ("落花生", "ピーナッツ"))):
            allergy_list.append(Allergie[6])
        if any(map(Nutritional_ingredients_value[1].__contains__, ("アーモンド", "あーもんど"))):
            allergy_list.append(Allergie[7])
        if any(map(Nutritional_ingredients_value[1].__contains__, ("あわび", "アワビ"))):
            allergy_list.append(Allergie[8])
        if any(map(Nutritional_ingredients_value[1].__contains__, ("いか", "イカ", "するめ", "スルメ"))):
            allergy_list.append(Allergie[9])
        if any(map(Nutritional_ingredients_value[1].__contains__, ("いくら", "イクラ", "すじこ", "スジコ"))):
            allergy_list.append(Allergie[10])
        if any(map(Nutritional_ingredients_value[1].__contains__, ("オレンジ", "おれんじ"))):
            allergy_list.append(Allergie[11])
        if any(map(Nutritional_ingredients_value[1].__contains__, ("カシューナッツ", "かしゅーなっつ"))):
            allergy_list.append(Allergie[12])
        if any(map(Nutritional_ingredients_value[1].__contains__, ("キウイフルーツ", "キウイ", "キウィー", "キーウィー", "キーウィ", "キウィ"))):
            allergy_list.append(Allergie[13])
        if any(map(Nutritional_ingredients_value[1].__contains__, ("牛", "ビーフ", "ぎゅうにく", "ぎゅう肉", "牛にく"))):
            allergy_list.append(Allergie[14])
        if any(map(Nutritional_ingredients_value[1].__contains__, ("くるみ", "クルミ"))):
            allergy_list.append(Allergie[15])
        if any(map(Nutritional_ingredients_value[1].__contains__, ("ごま", 'ゴマ', '胡麻'))):
            allergy_list.append(Allergie[16])
        if any(map(Nutritional_ingredients_value[1].__contains__, ("さけ", "鮭", "サケ", "サーモン", "しゃけ", "シャケ"))):
            allergy_list.append(Allergie[17])
        if any(map(Nutritional_ingredients_value[1].__contains__, ("さば", "鯖", "サバ"))):
            allergy_list.append(Allergie[18])
        if any(map(Nutritional_ingredients_value[1].__contains__, ("大豆", "だいず", "ダイズ", "醤油", "味噌", "豆腐", "油揚げ", "厚揚げ", "豆乳", "納豆", 'レシチン'))):
            allergy_list.append(Allergie[19])
        if any(map(Nutritional_ingredients_value[1].__contains__, ("鶏", "とり", "鳥", "チキン"))):
            allergy_list.append(Allergie[20])
            if any(map(Nutritional_ingredients_value[1].__contains__, ("鶏卵"))):
                allergy_list.pop()
        if any(map(Nutritional_ingredients_value[1].__contains__, ("バナナ", "ばなな"))):
            allergy_list.append(Allergie[21])
        if any(map(Nutritional_ingredients_value[1].__contains__, ("豚", "ぶた", "ポーク", "とんかつ", "トンカツ"))):
            allergy_list.append(Allergie[22])
        if any(map(Nutritional_ingredients_value[1].__contains__, ("まつたけ", "松茸", "マツタケ"))):
            allergy_list.append(Allergie[23])
        if any(map(Nutritional_ingredients_value[1].__contains__, ("もも", "モモ", "桃", "ピーチ"))):
            allergy_list.append(Allergie[24])
        if any(map(Nutritional_ingredients_value[1].__contains__, ("やまいも", "山芋", "ヤマイモ", "山いも", "とろろ", "ながいも"))):
            allergy_list.append(Allergie[25])
        if any(map(Nutritional_ingredients_value[1].__contains__, ("りんご", "リンゴ", "アップル"))):
            allergy_list.append(Allergie[26])
        if any(map(Nutritional_ingredients_value[1].__contains__, ("ゼラチン", "ぜらちん"))):
            allergy_list.append(Allergie[27])

        # for ike in range(Nutritional_ingredients_name_count):
        #     data = {
        #         Nutritional_ingredients_name[ike]:Nutritional_ingredients_value[ike]
        #     }
        # print(data)
        # count = 0
        # for hit in Tokenizer().tokenize(simple_name):
        #     pos = hit.part_of_speech.split(',')
        #     if '名詞' in pos:
        #         # print(hit.surface)
        #         Surface_type.append(hit.surface)  # 表層形を出力
        #         # count +=1
        #     # print(Surface_type)
        # print(Surface_type)

        # firestoreに追加
        # doc_ref = db.collection(u'product3').document(rand)
        # doc_ref.set({
        #     u'add_date': dt_now,
        #     u'allergy_id': allergy_list,
        #     u'brand_id': str(choco_brand_list.index(brand)),
        #     u'category_id': ['001', '004', '00'+str(category_a)],
        #     u'maker_id': '02zzgbAq1OxeXVMxoEhq',
        #     u'product_id': rand,
        #     u'product_name': simple_name_strip,
        #     u'raw_material': Nutritional_value_list[1],
        #     u'Internal_capacity': Nutritional_value_list[2],
        #     u'update_date': dt_now,
        #     u'images': [''],
        #     u'release_date': datetime.datetime(1, 1, 1, 1, 1, 1, 1),
        #     u'maker_url': url_list,
        #     u'delete_flag': False,
        #     u'delete_date': dt_now,
        #     u'Morphological_analysis': Morphological_analysis
        #     # u'gram':gram,
        # })
        # doc_ref.collection(u'nutritional_ingredients').document(rand).set({
        #     u'Nutritional_ingredients': Nutritional_ingredients_dick,
        #     u'subject': Nutritional_ingredients_subject_text
        # })
