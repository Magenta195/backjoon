###
# 3176. 도로 네트워크
# problem : https://www.acmicpc.net/problem/3176
# status : solved (Only pypy3)
###
import sys
from collections import deque
from math import log2
input = sys.stdin.readline
q = deque([1])
N = int(input())
l = int(log2(N)+1)

depth = [-1]*(N+1)
p = [[[0,0,0] for _ in range(l)] for _ in range(N+1)]
g = [list() for _ in range(N+1)]

for _ in range(N-1):
  a, b, d = map(int, input().split())
  g[a].append((b,d))
  g[b].append((a,d))

depth[1] = 1
while q :
  n = q.popleft()
  d = depth[n]
  for c, dis in g[n]:
    if depth[c] == -1 :
      depth[c] = d+1
      p[c][0][0] = n
      p[c][0][1] = dis
      p[c][0][2] = dis
      q.append(c)

for i in range(1, l):
  for j in range(1, N+1):
    p[j][i][1] = min(p[j][i-1][1], p[p[j][i-1][0]][i-1][1])
    p[j][i][2] = max(p[j][i-1][2], p[p[j][i-1][0]][i-1][2])
    p[j][i][0] = p[p[j][i-1][0]][i-1][0]

M = int(input())
for _ in range(M):
  a, b = map(int, input().split())
  min_dis, max_dis = float('inf'), 0
  if depth[a] < depth[b] : a, b = b, a
  diff = depth[a] - depth[b]
    
  for i in range(l-1, -1, -1):
    if diff & 1 << i :
      min_dis = min(min_dis, p[a][i][1])
      max_dis = max(max_dis, p[a][i][2])
      a = p[a][i][0]

  if a == b : 
    print(min_dis, max_dis)
    continue

  for i in range(l-1, -1, -1):
    if p[a][i][0] != p[b][i][0] :
      min_dis = min(min_dis, p[a][i][1], p[b][i][1])
      max_dis = max(max_dis, p[a][i][2], p[b][i][2])
      a, b = p[a][i][0], p[b][i][0]
  
  print(min(min_dis, p[a][0][1], p[b][0][1]), max(max_dis, p[a][0][2], p[b][0][2]))
