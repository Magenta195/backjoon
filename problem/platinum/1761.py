###
# 1761. 정점들의 거리
# problem : https://www.acmicpc.net/problem/1761
# status : solved
###
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e7))
l = 21
N = int(input())
depth = [-1]*N
dist = [0]*N
parent = [[0]*l for _ in range(N)]
g = {keys : [] for keys in range(N)}

for _ in range(N-1):
  a, b, d = map(int, input().split())
  g[a-1].append((b-1,d))
  g[b-1].append((a-1,d))

def dfs(n, d):
  depth[n] = d
  for c, dis in g[n]:
    if depth[c] > -1 : continue
    parent[c][0] = n
    dist[c] = dist[n] + dis
    dfs(c, d+1)

def set_parent():
  dfs(0,1)
  for i in range(1, l):
    for j in range(N):
      parent[j][i] = parent[parent[j][i-1]][i-1]

def check(a, b):
  dis = dist[a] + dist[b]
  if depth[a] < depth[b] : a, b = b, a
    
  for i in range(l-1, -1, -1):
    if depth[a] - depth[b] >= 2**i:
      a = parent[a][i]

  if a == b : return dis - dist[a]*2

  for i in range(l-1, -1, -1):
    if parent[a][i] != parent[b][i] :
      a, b = parent[a][i], parent[b][i]

  return dis - dist[parent[a][0]]*2
  

M = int(input())
set_parent()
for _ in range(M):
  a, b = map(int, input().split())
  print(check(a-1,b-1))
