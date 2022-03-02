###
# 1647. 도시 분할 계획
# problem : https://www.acmicpc.net/problem/1647
# status : solved
###

### trial 1(kruskal)
import sys
sys.setrecursionlimit(1000001)
input = sys.stdin.readline

n, m = map(int, input().split())
v = list(range(n+1))
d = 0
q = sorted([list(map(int, input().split())) for _ in range(m)], key = lambda x : -x[2])
def find(i):
  if v[i] == i : return i
  return find(v[i])

def union(x, y):
  ax = find(x)
  ay = find(y)
  if ax < ay : v[ay] = ax
  else : v[ax] = ay
  
cnt = 0
while q and cnt < n-2 :
  a,b,c = q.pop()
  if find(a) == find(b) : continue
  cnt += 1
  union(a, b)
  d += c

print(d)

### trial 2(prim, 시간 초과)

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m = map(int, input().split())
v = [False]*(n+1)
g = { key : [] for key in range(1, n+1) }
for a,b,c in [list(map(int, input().split())) for _ in range(m)]:
  g[a].append((b,c))
  g[b].append((a,c))

q, d = [(0,1,1)], 0
  
cnt = 0
while q and cnt < n-1 :
  c, a, b = heappop(q)
  if not v[b] :
    cnt += 1
    v[b] = True
    d += c
    for k, k_c in g[b]:
      heappush(q, (k_c, b, k))
    
print(d)
