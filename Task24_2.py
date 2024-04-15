# https://inf-ege.sdamgia.ru/problem?id=59729&ysclid=lv0lua2o1u741990644

with open('Task24_2.txt') as file:
    s = file.readline()

pos = []
for i in range(len(s)-1):
    if s[i]+s[i+1] == 'TT':
        pos.append(i)


res = []
for i, j in zip(pos, pos[149:]):
    res.append(j - i + 2)

print(min(res))
