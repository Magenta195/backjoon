###
# 13511. 트리와 쿼리 2
# problem : https://www.acmicpc.net/problem/13511
# status : solved
###

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())

MAX_length = 21
visited = [0]*N
parent = [[(0,0)]*MAX_length for _ in range(N)]
depth = [0]*N
edge = { key : [] for key in range(N)}
for _ in range(N-1):
  u, v, w = map(int, input().split())
  edge[u-1].append((v-1, w))
  edge[v-1].append((u-1, w))

def dfs(node, d):
  for next, weight in edge[node]:
    if not visited[next] :
      visited[next] = 1
      depth[next] = d
      parent[next][0] = (node, weight)
      dfs(next, d+1)

def init():
  dfs(0, 1)
  for i in range(1, MAX_length):
    for j in range(N):
      p, p_weight = parent[j][i-1]
      a, a_weight = parent[p][i-1]
      parent[j][i] = (a, p_weight+a_weight)

def LeastCommonAncester(u, v):
  if depth[u] < depth[v]: u,v = v, u

  diff = depth[u] - depth[v]
  diff_weight = 0
  for i in range(MAX_length-1,-1,-1):
    if diff & (1 << i) : 
      diff_weight += parent[u][i][1]
      u = parent[u][i][0]

  if u == v :
    return diff_weight, u
    
  for i in range(MAX_length-1, -1, -1):
    if parent[u][i][0] != parent[v][i][0] :
      diff_weight += parent[u][i][1]+parent[v][i][1]
      u, v = parent[u][i][0], parent[v][i][0]

  return diff_weight+parent[u][0][1]+parent[v][0][1], parent[v][0][0]

init()
M = int(input())
for _ in range(M):
  num, *query = map(int, input().split())
  if num == 1 :
    u, v = query
  else : 
    u, v, k = query
  u -= 1
  v -= 1
  weight, lca = LeastCommonAncester(u, v)
  
  if num == 1 :
    print(weight)
  else :
    k -= 1
    if depth[u]-depth[lca] >= k :
      node, diff = u, k
    else :
      node, diff = v, depth[v]-depth[lca]-(k-(depth[u]-depth[lca]))
    for i in range(MAX_length-1,-1,-1):
      if diff & (1 << i) : 
        node = parent[node][i][0]
    print(node+1)
