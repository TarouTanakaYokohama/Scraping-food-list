# import spacy
# import ginza

# nlp = spacy.load('ja_ginza')  # モデルのロード

# doc = nlp("メルティーキッス フルーティー濃いちご")
# Morphological_analysis = []
# a = []
# # i = 0
# for sent in doc.sents:
#     for token in sent:
#         # if token.pos_ in ('NOUN', 'PRON', 'PROPN','VERB'):
#             # a.pop()
#         Morphological_analysis.append(token.pos_)  # 表層形を出力
#         a.append(token.orth_)
#         if token.orth_ == '％' or token.orth_ == '袋':
#             a.pop()
# print(Morphological_analysis)
# print(a)

Nutritional_ingredients_value = ["",
                                 "小麦粉（国内製造）、砂糖、カカオマス、植物油脂、全粉乳、ココアバター、ライ麦粉、ショートニング、脱脂粉乳、麦芽エキス、バターシーズニング、練乳パウダー、カラメルソース、食塩／乳化剤、膨脹剤、香料、カラメル色素、（一部に小麦・乳成分・大豆を含む）"]
Allergie = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010', '011', '012',
            '013', '014', '015', '016', '017', '018', '019', '020', '021', '022', '023', '024', '025', '026', '027', '028']

allergy_list = []

if any(map(Nutritional_ingredients_value[1].__contains__, ("えび", "海老", "エビ"))):
    allergy_list.append(Allergie[0])
if any(map(Nutritional_ingredients_value[1].__contains__, ("かに", "蟹", "カニ","ガニ"))):
    allergy_list.append(Allergie[1])
if any(map(Nutritional_ingredients_value[1].__contains__, ("小麦", "こむぎ", "コムギ", "パン", "うどん"))):
    allergy_list.append(Allergie[2])
if any(map(Nutritional_ingredients_value[1].__contains__, ("そば", "ソバ"))):
    allergy_list.append(Allergie[3])
if any(map(Nutritional_ingredients_value[1].__contains__, ("卵白", "卵黄", "玉子", "たまご", "タマゴ", "エッグ", "鶏卵", "あひる卵", "うずら卵","マヨネーズ", "オムレツ", "目玉焼", "かに玉", "オムライス", "親子丼"))):
    allergy_list.append(Allergie[4])
if any(map(Nutritional_ingredients_value[1].__contains__, ("乳", "バター", "ホエイ", "アイスクリーム", "クリームパウダー", "ミルク", "生クリーム", "ヨーグルト", "アイス"))):
    allergy_list.append(Allergie[5])
if any(map(Nutritional_ingredients_value[1].__contains__, ("落花生", "ピーナッツ"))):
    allergy_list.append(Allergie[6])
if any(map(Nutritional_ingredients_value[1].__contains__, ("アーモンド","あーもんど"))):
    allergy_list.append(Allergie[7])
if any(map(Nutritional_ingredients_value[1].__contains__, ("あわび", "アワビ"))):
    allergy_list.append(Allergie[8])
if any(map(Nutritional_ingredients_value[1].__contains__, ("いか", "イカ", "するめ", "スルメ"))):
    allergy_list.append(Allergie[9])
if any(map(Nutritional_ingredients_value[1].__contains__, ("いくら", "イクラ", "すじこ", "スジコ"))):
    allergy_list.append(Allergie[10])
if any(map(Nutritional_ingredients_value[1].__contains__, ("オレンジ","おれんじ"))):
    allergy_list.append(Allergie[11])
if any(map(Nutritional_ingredients_value[1].__contains__, ("カシューナッツ","かしゅーなっつ"))):
    allergy_list.append(Allergie[12])
if any(map(Nutritional_ingredients_value[1].__contains__, ("キウイフルーツ", "キウイ", "キウィー", "キーウィー", "キーウィ", "キウィ"))):
    allergy_list.append(Allergie[13])
if any(map(Nutritional_ingredients_value[1].__contains__, ("牛", "ビーフ", "ぎゅうにく", "ぎゅう肉", "牛にく"))):
    allergy_list.append(Allergie[14])
if any(map(Nutritional_ingredients_value[1].__contains__, ("くるみ", "クルミ"))):
    allergy_list.append(Allergie[15])
if any(map(Nutritional_ingredients_value[1].__contains__, ("ごま",'ゴマ','胡麻'))):
    allergy_list.append(Allergie[16])
if any(map(Nutritional_ingredients_value[1].__contains__, ("さけ", "鮭", "サケ", "サーモン", "しゃけ", "シャケ"))):
    allergy_list.append(Allergie[17])
if any(map(Nutritional_ingredients_value[1].__contains__, ("さば", "鯖", "サバ"))):
    allergy_list.append(Allergie[18])
if any(map(Nutritional_ingredients_value[1].__contains__, ("大豆", "だいず", "ダイズ", "醤油", "味噌", "豆腐", "油揚げ", "厚揚げ", "豆乳", "納豆"))):
    allergy_list.append(Allergie[19])
if any(map(Nutritional_ingredients_value[1].__contains__, ("鶏", "とり", "鳥", "チキン"))):
    allergy_list.append(Allergie[20])
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
if any(map(Nutritional_ingredients_value[1].__contains__, ("ゼラチン","ぜらちん"))):
    allergy_list.append(Allergie[27])


print(allergy_list)
