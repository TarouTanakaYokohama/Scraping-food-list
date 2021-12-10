import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(
    "./umyfoods-rac-firebase-adminsdk-m6vos-476571680f.json")  # ダウンロードした秘密鍵
firebase_admin.initialize_app(cred)

db = firestore.client()
# docs = db.collection('major_category').limit_to_last(1)
# query = docs.order_by("brand_id").limit_to_last(2)
# query = docs
# docs_list = docs.get()
# Import database module.
# from firebase_admin import db

db = firestore.client()
docs = db.collection('major_category').get()
for doc in docs:
    print(doc.to_dict())


# for doc in docs_list:
#     # print(docs_list)
#     print(type(str(doc.to_dict()['category_id'])))

# for doc in docs_list:
#     if doc.to_dict()['brand_id'] == '1':
#         print(doc.to_dict()['product_name'])

# for doc in docs_list:
#     # if doc.to_dict()['brand_id'] == '10':
#     print(type(int(doc.to_dict()['brand_id'])))
