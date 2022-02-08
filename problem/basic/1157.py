s = input().upper()
d = list(set(s))
cnt = []

for x in d :
    cnt.append(s.count(x))

if cnt.count(max(cnt)) > 1 :
    print('?')
else :
    print(d[cnt.index(max(cnt))])
