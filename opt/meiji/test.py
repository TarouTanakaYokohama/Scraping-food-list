# a = ['名称', '原材料名', '内容量', '保存方法', 'エネルギー', 'たんぱく質', '脂質', '炭水化物', '－糖質', '－食物繊維', '食塩相当量']
# b = ['チョコレート', '砂糖（外国製造）、カカオマス、全粉乳、ココアバター／レシチン、香料、（一部に乳成分・大豆を含む）', '50g', '28℃以下の涼しい場所で保存してください。', '283kcal', '3.8g', '18.4g', '26.7g', '24.5g', '2.2g', '0.065g']
# d = {}
# for i in range(len(a)-4):
#     d |= {a[i+4]:b[i+4]}
#     # a[i+3],b[i+3]
# print(d)

Allergie = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010', '011', '012',
            '013', '014', '015', '016', '017', '018', '019', '020', '021', '022', '023', '024', '025', '026', '027', '028']

Nutritional_ingredients_name = ['']
Nutritional_ingredients_value = ['','鶏卵']

Nutritional_ingredients_dick = {}
for i in range(len(Nutritional_ingredients_name)-4):
    Nutritional_ingredients_dick |= {Nutritional_ingredients_name[i+4]:Nutritional_ingredients_value[i+4]}

# 原材料からアレルギーを取得
allergy_list = []

if any(map(Nutritional_ingredients_value[1].__contains__, ("えび", "海老", "エビ"))):
    allergy_list.append(Allergie[0])
if any(map(Nutritional_ingredients_value[1].__contains__, ("かに", "蟹", "カニ","ガニ","がに"))):
    allergy_list.append(Allergie[1])
if any(map(Nutritional_ingredients_value[1].__contains__, ("小麦", "こむぎ", "コムギ", "パン", "うどん",'デュラムセモリナ'))):
    allergy_list.append(Allergie[2])
if any(map(Nutritional_ingredients_value[1].__contains__, ("そば", "ソバ"))):
    allergy_list.append(Allergie[3])
if any(map(Nutritional_ingredients_value[1].__contains__, ("卵白", "卵黄", "玉子", "たまご", "タマゴ", "エッグ", "鶏卵", "あひる卵", "うずら卵","マヨネーズ", "オムレツ", "目玉焼", "かに玉", "オムライス", "親子丼",'卵殻カルシウム'))):
    allergy_list.append(Allergie[4])
if any(map(Nutritional_ingredients_value[1].__contains__, ("生乳","牛乳","特別牛乳","成分調整牛乳""低脂肪牛乳","無脂肪牛乳","加工乳","乳製品","バター","バターオイル","チーズ","濃縮ホエイ","アイスクリーム","濃縮乳","脱脂濃縮乳","無糖れん乳","無糖練乳","無糖脱脂れん乳","無糖脱脂練乳","加糖れん乳","加糖練乳","加糖脱脂れん乳","加糖脱脂練乳","全粉乳","脱脂粉乳","たんぱく質濃縮","バターミルクパウダー","加糖粉乳","調製粉乳","発酵乳","はっ酵乳","乳酸菌飲料","乳飲料","カゼイン","生クリーム","ヨーグルト","アイスミルク","ラクトアイス","ミルク","乳成分"))):
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
if any(map(Nutritional_ingredients_value[1].__contains__, ("大豆", "だいず", "ダイズ", "醤油", "味噌", "豆腐", "油揚げ", "厚揚げ", "豆乳", "納豆",'レシチン'))):
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
if any(map(Nutritional_ingredients_value[1].__contains__, ("ゼラチン","ぜらちん"))):
    allergy_list.append(Allergie[27])

print(allergy_list)