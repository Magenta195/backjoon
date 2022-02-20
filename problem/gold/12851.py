###
# 12851. 숨바꼭질 2
# problem : https://www.acmicpc.net/problem/12851
# status : solved
###
n, k = map(int, input().split())
v = [[-1,0] for _ in range(100001)]
v[n][0] = 0
v[n][1] = 1
q = [n]

flg = True
while q :
  x = q.pop(0)
  if x == k :
    flg = False
  if flg :
    for ax in [x-1, x+1, 2*x]:
      if -1<ax<100001:
        if v[ax][0] == -1:
          q.append(ax)
          v[ax][0] = v[x][0] + 1
          v[ax][1] = v[x][1]
        elif v[ax][0] == v[x][0] + 1:
          v[ax][1] += v[x][1]

print(v[k][0])
print(v[k][1])
