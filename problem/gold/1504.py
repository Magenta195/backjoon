###
# 1504. 특정한 최단 경로
# problem : https://www.acmicpc.net/problem/1504
# status : 
###
import sys
import heapq

n, e = map(int, sys.stdin.readline().split())
v = [[1e10]*n for _ in range(n)]
for i in range(n) : v[i][i] = 0
for a, b, c in [list(map(int, sys.stdin.readline().split())) for _ in range(e)]:
  v[a-1][b-1] = c
  v[b-1][a-1] = c

v1, v2 = map(int, sys.stdin.readline().split())

def dijkstra(start, end):
  d_lst = [1e10]*n
  q = [(0, start)]
  while q :
    d, i = heapq.heappop(q)
    if d_lst[i] < d : continue
    for j, v_d in enumerate(v[i]) :
      if v_d + d < d_lst[j] :
        d_lst[j] = v_d + d
        heapq.heappush(q, (v_d + d, j))
  return d_lst[end]

mid = dijkstra(v1-1, v2-1)
d1 = dijkstra(0, v1-1) + dijkstra(v2-1, n-1) + mid
d2 = dijkstra(0, v2-1) + dijkstra(v1-1, n-1) + mid

print(-1 if min(d1,d2) >= 1e10 else min(d1,d2))
