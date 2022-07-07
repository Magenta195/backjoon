###
# 3584. 가장 가까운 공통 조상
# problem : 
# status : solved
# time : 00:40:00 + alpha
###

### trial 1. O(logn)

import sys
input = sys.stdin.readline
MAX = 15
sys.setrecursionlimit(10**6)
def dfs(node, depth):
  d[node] = depth
  
  for next in edge[node]:
    p[next][0] = node  
    dfs(next, depth+1)

for _ in range(int(input())):
  N = int(input())
  p = [[i]*MAX for i in range(N)]
  d = [0]*N
  visited = [False]*N
  visited[0] = True
  edge = { key : [] for key in range(N)}
  root = [True]*N
  for _ in range(N-1):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    root[b-1] = False

  r = root.index(True)
  dfs(r,0)
  for i in range(1, MAX):
    for j in range(N):
      p[j][i] = p[p[j][i-1]][i-1]

  a, b = map(int, input().split())
  a -= 1
  b -= 1
  if d[a] < d[b] : a,b = b,a
  diff = d[a] - d[b]

  if diff > 0 :
    for i in range(MAX-1,-1,-1):
      if diff & (1 << i) :
        a = p[a][i]

  if a == b :
    print(a+1)
    continue
  for i in range(MAX-1,-1,-1):
    if p[a][i] != p[b][i] :
      a, b = p[a][i], p[b][i]
  print(p[a][0]+1)
    
# trial 2. O(N)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(node, depth):
  d[node] = depth
  for next in edge[node]:
    p[next] = node  
    dfs(next, depth+1)

for _ in range(int(input())):
  N = int(input())
  p, d = list(range(N+1)), [0]*(N+1)
  edge = { key : [] for key in range(N+1)}
  root = [True]*(N+1)
  root[0] = False
  for _ in range(N-1):
    a, b = map(int, input().split())
    edge[a].append(b)
    root[b] = False
  r = root.index(True)
  dfs(r,0)

  a, b = map(int, input().split())
  if d[a] < d[b] : a,b = b,a
  diff = d[a] - d[b]

  if diff > 0 :
    for _ in range(diff) : a = p[a]

  if a == b :
    print(a)
    continue
  while True:
    if p[a] == p[b]: break
    a, b = p[a], p[b]
  print(p[a])


