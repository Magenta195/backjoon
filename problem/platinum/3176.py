###
# 3176. 도로 네트워크
# problem : https://www.acmicpc.net/problem/3176
# status : not solved
###
import sys
from collections import deque
from math import log2
input = sys.stdin.readline
sys.setrecursionlimit(int(1e7))
l = 21
q = deque([(0,1)])
N = int(input())
l = int(log2(N)+1)

depth = [-1]*N
dist = [[(float('inf'),0)]*l for _ in range(N)]
parent = [[0]*l for _ in range(N)]
g = {keys : [] for keys in range(N)}

for _ in range(N-1):
  a, b, d = map(int, input().split())
  g[a-1].append((b-1,d))
  g[b-1].append((a-1,d))

depth[0] = 1
while q :
  n, d = q.popleft()
  for c, dis in g[n]:
    if depth[c] > -1 : continue
    depth[c] = d+1
    q.append((c,d+1))
    parent[c][0] = n
    dist[c][0] = (dis,dis)

for i in range(1, l):
  for j in range(N):
    amin, amax = dist[j][i-1]
    bmin, bmax = dist[parent[j][i-1]][i-1]
    dist[j][i] = (min(amin, bmin), max(amax,bmax))
    parent[j][i] = parent[parent[j][i-1]][i-1]

M = int(input())
for _ in range(M):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  min_dis, max_dis = float('inf'), 0
  if depth[a] < depth[b] : a, b = b, a
    
  for i in range(l-1, -1, -1):
    if depth[a] - depth[b] >= 2**i:
      min_dis = min(min_dis, dist[a][i][0])
      max_dis = max(max_dis, dist[a][i][1])
      a = parent[a][i]

  if a == b : 
    print(min_dis, max_dis)
    continue

  for i in range(l-1, -1, -1):
    if parent[a][i] != parent[b][i] :
      min_dis = min(min_dis, dist[a][i][0], dist[b][i][0])
      max_dis = max(max_dis, dist[a][i][1], dist[b][i][1])
      a, b = parent[a][i], parent[b][i]
  
  print(min(min_dis, dist[a][0][0], dist[b][0][0]), max(max_dis, dist[a][0][1], dist[b][0][1]))
