###
# 1647. 도시 분할 계획
# problem : https://www.acmicpc.net/problem/1647
# status : 
###

### trial 1(kruskal, 시간 초과)
import sys
from heapq import heappush, heappop
sys.setrecursionlimit(1000001)
input = sys.stdin.readline

n, m = map(int, input().split())
v = list(range(n+1))
q, d = [], []
for a,b,c in [list(map(int, input().split())) for _ in range(m)]:
  heappush(q, (c, a, b))

def find(i):
  if v[i] == i : return i
  return find(v[i])
  
def union(x, y):
  v[find(x)] = find(y)
  
cnt = 0
while q and cnt < n-1 :
  c,a,b = heappop(q)
  if find(a) == find(b) : continue
  cnt += 1
  union(a, b)
  heappush(d, -c)
heappop(d)  
print(-sum(d))

### trial 2

import sys
from heapq import heappush, heappop
sys.setrecursionlimit(1000001)
input = sys.stdin.readline

n, m = map(int, input().split())
v = [False]*(n+1)
g = { key : [] for key in range(1, n+1) }
for a,b,c in [list(map(int, input().split())) for _ in range(m)]:
  g[a].append((b,c))
  g[b].append((a,c))

q, d = [(0,1,1)], []  
  
cnt = 0
while q and cnt < n-1 :
  c, a, b = heappop(q)
  cnt += 1
  v[b] = True
  heappush(d, -c)
  for k, k_c in g[b]:
    if not v[k] : heappush(q, (b, k, k_c))
heappop(d)
    
print(-sum(d))
