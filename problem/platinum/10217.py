###
# 10217. KCM Travel
# problem : https://www.acmicpc.net/problem/10217
# status : solved
# time : 00:53:00
###

import sys
from collections import deque

input = sys.stdin.readline
INF = float('inf')
for _ in range(int(input())):
  N, M, K = map(int,input().split())
  lst = [[] for keys in range(N)]

  for _ in range(K):
    u, v, c, d = map(int,input().split())
    lst[u-1].append((v-1,c,d))
  
  q = deque([(0,0,0)])
  d_lst = [[INF]*(M+1) for _ in range(N)]
  d_lst[0][0] = 0
  
  while q :
    dist, cost, start = q.popleft()
    if d_lst[start][cost] < dist : continue
    for end, c, dis in lst[start] :
      d = dist+dis
      if c + cost <= M and d_lst[end][c+cost] > d: 
        for i in range(c+cost,M+1):
          if d_lst[end][i] > d :
            d_lst[end][i] = d
          else : 
            break
        q.append((d,c+cost,end))
  ans = d_lst[-1][-1]
  print(ans if ans < INF else 'Poor KCM')
