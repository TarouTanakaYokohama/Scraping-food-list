import random
import string
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

choco_brand_list = ['','ミルクチョコレート','明治 ザ・チョコレート','アーモンドチョコレート','マカダミアチョコレート','その他ナッツチョコレート','きのこの山','たけのこの里','きのこの山とたけのこの里','チョコレート効果','オリゴスマート','明治TANPACT','エムズバー','ガルボ','フラン','ホルン','プッカ','アグロフォレストリーミルクチョコレート','MyチョコBox','小粒チョコ','リッチチョコサンド']

brand_count = len(choco_brand_list)

# Use a service account
cred = credentials.Certificate('../umyfoods-rac-firebase-adminsdk-m6vos-476571680f.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
dat = string.digits + string.ascii_lowercase + string.ascii_uppercase
rand = ''.join([random.choice(dat) for i in range(19)])

number = 0

doc_ref = db.collection(u'brand').document('rand')
doc_ref.set({
    u'brand_id': number+brand_count,
    u'brand_name': choco_brand_list[number]
})