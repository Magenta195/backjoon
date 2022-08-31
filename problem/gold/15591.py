###
# 15591. Mootube(Silver)
# problem : https://www.acmicpc.net/problem/15591
# status : solved
# time : 00:41:39
###

N, Q = map(int, input().split())
MAX = float('inf')
edge_dict = { key : [] for key in range(1, N+1)}

for _ in range(N-1):
  p, q, r = map(int, input().split())
  edge_dict[p].append((q, r))
  edge_dict[q].append((p, r))

def dfs(start, max_usado):
  visited = [False]*(N+1)
  visited[start] = True
  q = [(start, MAX)]
  while q :
    node, usado = q.pop()
    for leaf, leaf_usado in edge_dict[node] :
      if not visited[leaf] and leaf_usado >= max_usado :
        visited[leaf] = True
        q.append((leaf, leaf_usado))

  return visited.count(True)-1

for _ in range(Q):
  k, v = map(int, input().split())
  print(dfs(v, k))
