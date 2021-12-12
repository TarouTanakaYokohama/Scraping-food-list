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

db = firestore.client()
# docs = db.collection('major_category').get()
# for doc in docs:
#     print(doc.to_dict())
Allergie = []
aaa = '018'

fafafa = '003'
for i in range(3):
    if i <10:
        Allergie.append('00'+str(i))
    else :
        Allergie.append('0'+str(i))
    doc_ref = db.collection('major_category').document(aaa)
    doc_ref.collection(u'category').document(fafafa).collection(u'sub_category').document(str(Allergie[i])).set({
          'category_id': str(Allergie[i])
        },merge=True)
    # doc_ref.set({
    #     'category_id': str(Allergie[i])
    #     },merge=True)

# doc_ref = db.collection(u'major_category').document(u'001')

# doc = doc_ref.get()
# if doc.exists:
#     print(f'Document data: {doc.to_dict()}')
# else:
#     print(u'No such document!')


# for doc in docs_list:
#     # print(docs_list)
#     print(type(str(doc.to_dict()['category_id'])))

# for doc in docs_list:
#     if doc.to_dict()['brand_id'] == '1':
#         print(doc.to_dict()['product_name'])

# for doc in docs_list:
#     # if doc.to_dict()['brand_id'] == '10':
#     print(type(int(doc.to_dict()['brand_id'])))
