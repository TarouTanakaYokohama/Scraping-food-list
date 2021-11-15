from janome.tokenizer import Tokenizer

s = '明治ハイミルクチョコレート CUBIE'

for tok in Tokenizer().tokenize(s):
    pos = tok.part_of_speech.split(',')
    if '名詞' in pos:
        print(tok.surface)  # 表層形を出力
