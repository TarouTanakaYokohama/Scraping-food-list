import random
import string
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

# Use a service account
cred = credentials.Certificate('umyfoods-rac-firebase-adminsdk-m6vos-476571680f.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# 現時刻取得
dt_now = datetime.datetime.now()

# id作成
dat = string.digits + string.ascii_lowercase + string.ascii_uppercase
rand = ''.join([random.choice(dat) for i in range(19)])

# firestoreに追加
doc_ref = db.collection(u'product').document(rand)
doc_ref.set({
    u'add_date': dt_now,
    u'allergy_id': ['006'],
    u'brand_id': u'003',
    u'category_id': ['001','007','001'],
    u'maker_id':'001',
    u'product_id': rand,
    u'product_name': u'午後の紅茶',
    u'raw_material': u'水,小茶,乳',
    u'update_date': dt_now
})