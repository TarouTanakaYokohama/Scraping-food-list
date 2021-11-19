import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('./umyfoods-rac-firebase-adminsdk-m6vos-476571680f.json')

firebase_admin.initialize_app(cred)

db = firestore.client()

allergy_name = ['えび','かに','小麦','そば','卵','乳','落花生','アーモンド','あわび','いか','いくら','オレンジ','カシューナッツ','キウイフルーツ','牛肉','くるみ','ごま','さけ','さば','大豆','鶏肉','バナナ','豚肉','まつたけ','もも','やまいも','りんご','ゼラチン']
for a in range(28):
    a+=1
    if a < 10:
        allergy_id ='00'+str(a)
    else: allergy_id ='0'+str(a)
    doc_ref = db.collection(u'allergy').document(allergy_id)
    doc_ref.set({
        u'allergy_id': allergy_id,
        u'allergy_name': allergy_name[a-1],
    })