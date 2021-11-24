a = '栄養成分表示 1箱（84g）あたり'
a = '栄養成分表示 きのこの山いちご＆ショコラ 1袋（12g）あたり'

# b = a.split()

v = []
for i,s in enumerate(a.split()):
    if i != 0:
        v.append(s)
print(' '.join(v))
