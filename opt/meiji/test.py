import spacy
# import ginza

nlp = spacy.load('ja_ginza')  # モデルのロード

doc = nlp("メルティーキッス フルーティー濃いちご")
Morphological_analysis = []
a = []
# i = 0
for sent in doc.sents:
    for token in sent:
        # if token.pos_ in ('NOUN', 'PRON', 'PROPN','VERB'):
            # a.pop()
        Morphological_analysis.append(token.pos_)  # 表層形を出力
        a.append(token.orth_)
        if token.orth_ == '％' or token.orth_ == '袋':
            a.pop()
print(Morphological_analysis)
print(a)