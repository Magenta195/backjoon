###
# 1774. 우주신과의 교감
# problem : https://www.acmicpc.net/problem/1774
# status : solved
# time : ???
###

### 1. prim

from heapq import heappush, heappop
N, M = map(int, input().split())
MAX = float('inf')
coord = [tuple(map(int, input().split())) for _ in range(N)]
dist = [[0]*N for _ in range(N)]

for i in range(N-1):
  for j in range(i+1,N):
    dist[i][j] = dist[j][i] = ((coord[i][0]-coord[j][0])**2+(coord[i][1]-coord[j][1])**2)**0.5

for _ in range(M):
  a, b = map(int, input().split())
  dist[a-1][b-1] = dist[b-1][a-1] = 0

dis_mat = [MAX]*N
q = [(0,0)]
cnt, ans = 0, 0

while q :
  d, start = heappop(q)
  if dis_mat[start] < MAX : continue
  cnt += 1
  dis_mat[start] = d
  ans += d
  if cnt == N : break
  for end, new_d in enumerate(dist[start]) :
    if dis_mat[end] == MAX : heappush(q, (new_d, end))
print('%.2f'%(ans))

### 2. kruskal

import math

N, M = map(int, input().split())
MAX = float('inf')
coord = [tuple(map(int, input().split())) for _ in range(N)]
dist = [[0]*N for _ in range(N)]
dis_mat = []
p = list(range(N))

def find(x):
  if p[x] == x :
    return x
  p[x] = find(p[x])
  return p[x]

def union(dx, dy):
  if dx < dy :
    p[dy] = dx
  else :
    p[dx] = dy

cnt = 0
for _ in range(M):
  a, b = map(int, input().split())
  da, db = find(a-1), find(b-1)
  if da != db :
    union(da, db)
    cnt += 1

for i in range(N-1):
  for j in range(i+1,N):
    dis = math.sqrt((coord[i][0]-coord[j][0])**2+(coord[i][1]-coord[j][1])**2)
    dis_mat.append((dis,i,j))
dis_mat.sort()

ans = 0
for dis, i, j in dis_mat :
  di, dj = find(i), find(j)
  if di != dj :
    union(di, dj)
    ans += dis
    cnt += 1
  if cnt == N-1 : break

print('%.2f'%(ans))
