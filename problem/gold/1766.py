###
# 1766. 문제집
# problem : https://www.acmicpc.net/problem/1766
# status : 
###

import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n, m = map(int, sys.stdin.readline().split())
g = { key : [] for key in range(1, n+1) }
d = [0]*(n+1)

for a, b in [list(map(int, sys.stdin.readline().split())) for _ in range(m)]:
  g[a].append(b)
  d[b] += 1

lst = []
q = []
for i in range(1, n+1):
  if d[i] == 0: 
    heappush(q, i)

while q:
  a = heappop(q)
  lst.append(a)
  
  for i in g[a] :
    d[i] -= 1
    if d[i] == 0 :
      heappush(q, i)
  
print(*lst)
