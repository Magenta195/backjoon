###
# 13907. 세금
# problem : https://www.acmicpc.net/problem/13907
# status : solved
###

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = float('inf')

def dijkstra():
  q = [(0,S,0)]
  while q :
    dis, start, depth = heappop(q)
    flag = False
    for past_dis in distance[start][:depth+1]:
        if past_dis < dis :
            flag = True
            break
    if flag or start == D: continue
    for end, new_dis in e[start] :
      cur_dis = dis + new_dis
      if depth+1 < N and cur_dis < distance[end][depth+1]:
        distance[end][depth+1] = cur_dis
        heappush(q, (cur_dis, end, depth+1))

N, M, K = map(int, input().split())
S, D = map(int, input().split())
e = [[] for _ in range(N+1)]
distance = [[INF]*N for _ in range(N+1)]
distance[S][0] = 0
for _ in range(M):
  a, b, w = map(int, input().split())
  e[a].append((b,w))
  e[b].append((a,w))

dijkstra()
print(min(distance[D]))
for _ in range(K):
  tax = int(input())
  for i in range(N):
    if distance[D][i] == INF : continue
    distance[D][i] += i*tax
  print(min(distance[D]))
