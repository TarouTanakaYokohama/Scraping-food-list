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

# 001えび
# 002かに
# 003小麦
# 004そば
# 005卵
# 006乳
# 007落花生
# 008あわび
# 009いか
# 010いくら
# 011オレンジ
# 012カシューナッツ
# 013キウイフルーツ
# 014牛肉
# 015くるみ
# 016ごま
# 017さけ
# 018さば
# 019大豆
# 020鶏肉
# 021バナナ
# 022豚肉
# 023まつたけ
# 024もも
# 025やまいも
# 026りんご
# 027ゼラチン
# 028カカオ
Nutritional_ingredients_value = ["",
                                 "小麦粉（国内製造）、砂糖、カカオマス、植物油脂、全粉乳、ココアバター、ライ麦粉、ショートニング、脱脂粉乳、麦芽エキス、バターシーズニング、練乳パウダー、カラメルソース、食塩／乳化剤、膨脹剤、香料、カラメル色素、（一部に小麦・乳成分・大豆を含む）"]
Allergie = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010', '011', '012',
            '013', '014', '015', '016', '017', '018', '019', '020', '021', '022', '023', '024', '025', '026', '027']

a = []
# print(x)
Shrimp = "小麦" in Nutritional_ingredients_value[1]
if Shrimp == True:
    a.append(Allergie[3])
else:
    a.append(Allergie[1])
print(a)
# print(Allergie)
