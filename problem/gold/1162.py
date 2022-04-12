###
# 1162. 도로포장
# problem : https://www.acmicpc.net/problem/1162
# status : solved
###

import sys
from heapq import heappush, heappop
input = sys.stdin.readline
MAX = float('inf')

N, M, K = map(int, input().split())
edge = { keys : [] for keys in range(1, N+1)}
for _ in range(M):
  a, b, d = map(int, input().split())
  edge[a].append((b, d))
  edge[b].append((a, d))

def dijkstra():
  distance = [[MAX]*(K+1) for _ in range(N+1)]
  distance[1][K] = 0
  q = [(0, 1, K)]
  while q:
    dis, start, left_zero = heappop(q)
    if distance[start][left_zero] < dis : continue
    for end, new_dis in edge[start]:
      if dis + new_dis < distance[end][left_zero]:
        distance[end][left_zero] = dis + new_dis
        heappush(q, (dis+new_dis, end, left_zero))
      if left_zero > 0 and dis < distance[end][left_zero-1]:
        distance[end][left_zero-1] = dis
        heappush(q, (dis, end, left_zero-1))
   
  return distance

print(min(dijkstra()[N]))
      
      
    
  
  
  
