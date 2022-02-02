import random
import string
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# # Use a service account
cred = credentials.Certificate('../umyfoods-rac-firebase-adminsdk-m6vos-476571680f.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
dat = string.digits + string.ascii_lowercase + string.ascii_uppercase
rand = ''.join([random.choice(dat) for i in range(19)])

maker_name = "ヤガイ"

brand_id = '1'
brand_name = "おやつカルパス"

doc_ref = db.collection(u'maker').document(rand)
doc_ref.set({
    u'maker_id': rand,
    u'maker_name': maker_name
})
db = firestore.client()
dat = string.digits + string.ascii_lowercase + string.ascii_uppercase
doc_ref.collection(u'brand').document(rand).set({
    u'brand_id': brand_id,
    u'brand_name': brand_name
})
