###
# 1238. 파티
# problem : https://www.acmicpc.net/problem/1238
# status : solved
###

# trial 1
import sys
import heapq
input = sys.stdin.readline
n, m, x = map(int, input().split())
v = [[1e8]*n for _ in range(n)]
for s, e, t in [list(map(int, input().split())) for _ in range(m)]:
  v[s-1][e-1] = t

def dijkstra(start, end):
  q = [(0, start)]
  d = [1e8]*n
  d[start] = 0
  
  while q:
    dis, p = heapq.heappop(q)
    if d[p] < dis : continue
    for i, v_dis in enumerate(v[p]) :
      if v_dis + dis < d[i] :
        d[i] = v_dis + dis
        heapq.heappush(q, (v_dis + dis, i))
  return d[end]
d_lst = [(dijkstra(i, x-1) + dijkstra(x-1, i)) for i in range(n)]

print(max(d_lst))

# trial 2
import sys
import heapq
input = sys.stdin.readline
n, m, x = map(int, input().split())
v = {key : [] for key in range(1, n+1)}
for s, e, t in [list(map(int, input().split())) for _ in range(m)]:
  v[s].append((e, t))

def dijkstra(start, end):
  q = [(0, start)]
  d = [1e8]*(n+1)
  d[start] = 0
  
  while q:
    dis, p = heapq.heappop(q)
    if d[p] < dis : continue
    for i, v_dis in v[p] :
      if v_dis + dis < d[i] :
        d[i] = v_dis + dis
        heapq.heappush(q, (v_dis + dis, i))
  return d[end]
d_lst = [(dijkstra(i, x) + dijkstra(x, i)) for i in range(1, n+1)]

print(max(d_lst))
