###
# 4386. 별자리 만들기
# problem : https://www.acmicpc.net/problem/4386
# status : solved
###
import math
from heapq import heappush, heappop

n = int(input())
lst = [list(map(float, input().split())) for _ in range(n)]
g = [[0]*n for _ in range(n)]

for i in range(n):
  for j in range(n):
    if i == j : continue
    x1, y1 = lst[i]
    x2, y2 = lst[j]
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    g[i][j] = d
    g[j][i] = d

v = [False]*n
q = [(0, 0, 0)]
s = 0.
while q :
  dist, start, end = heappop(q)
  if v[end] : continue
  v[end] = True
  s += dist
  for i, new_d in enumerate(g[end]):
    if not v[i] :
      heappush(q, (new_d, end, i))

print('{:.2f}'.format(s))

