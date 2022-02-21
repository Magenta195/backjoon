###
# 15686. 치킨 배달
# problem : https://www.acmicpc.net/problem/15686
# status : solved
###

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

house = []
chk = []

for i in range(n):
  for j in range(n):
    if lst[i][j] == 1:
      house.append((j, i))
    elif lst[i][j] == 2:
      chk.append((j, i))
v = [True]*len(chk)
      
def price(t, s):
  if t == m:
    opt = 0
    for j in range(len(house)):
      tmp = 1e10
      for i in range(len(chk)):
        if v[i] : continue
        tmp = min(tmp, abs(house[j][0]-chk[i][0])+abs(house[j][1]-chk[i][1]))
      opt += tmp
    return opt
  
  opt = 1e10
  for i in range(s, len(chk)):
    v[i] = False
    opt = min(opt, price(t+1, i+1))
    v[i] = True
  return opt

print(price(0,0))
  
  
