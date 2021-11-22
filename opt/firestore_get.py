import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./umyfoods-rac-firebase-adminsdk-m6vos-476571680f.json") # ダウンロードした秘密鍵
firebase_admin.initialize_app(cred)

db = firestore.client()
docs = db.collection('product')
query = docs.order_by("brand_id").limit_to_last(2)
# query = docs
docs_list = query.get()

# for doc in docs_list:
#     if doc.to_dict()['brand_id'] == '10':
#         print(doc.to_dict()['product_name'])

for doc in docs_list:
    # if doc.to_dict()['brand_id'] == '10':
    print(type(int(doc.to_dict()['brand_id'])))

