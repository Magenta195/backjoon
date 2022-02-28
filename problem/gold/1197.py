###
# 1197. 최소 스패닝 트리
# problem : https://www.acmicpc.net/problem/1197
# status : solved
###

### trial 1 (러프한 kruskal MST, 시간초과)
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
lst = list(map(int, input().split())).sorted(key = lambda x:x[2])
g = []
c = 0
for i in list :
  if i[0] in g and i[1] in g : continue
  g.append(i[0])
  g.append(i[1])
  c += i[2]
print(c)

### trial 2 (Prim MST)
import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
visited = [False]*v
g = { key : [] for key in range(1,v+1) }
for _ in range(e):
  a, b, c = map(int, input().split())
  g[a].append((b, c))
  g[b].append((a, c))
  
q = [(0,1,1)]
c = 0
while q :
  cost, start, end = heapq.heappop(q)
  if not visited[end-1]:
    c += cost
    visited[end-1] = True
    for new_end, new_cost in g[end] :
      heapq.heappush(q, (new_cost, end, new_end))
print(c)
