###
# 10282. 해킹
# problem : https://www.acmicpc.net/problem/10282
# status : solved(pypy3)
# time : 00:14:01
###

import sys
from heapq import heappush, heappop
MAX = float("inf")
for _ in range(int(input())):
  n, d, c = map(int, input().split())
  q = [(0, c-1)]
  dist = [MAX]*n
  dist[c-1] = 0
  edge = { keys : [] for keys in range(n)}
  for _ in range(d):
    a, b, s = map(int, input().split())
    edge[b-1].append((a-1, s))

  while q:
    dis, start = heappop(q)
    if dist[start] < dis : continue
    for end, new_dis in edge[start] :
      if dist[end] > dis + new_dis :
        dist[end] = dis + new_dis
        heappush(q, (dis+new_dis, end))

  ans, cnt = 0, 0
  for dis in dist :
    if dis < MAX :
      cnt += 1
      ans = max(ans, dis)
  print(cnt, ans)
