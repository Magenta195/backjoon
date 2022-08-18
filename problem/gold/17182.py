###
# 17182. 우주 탐사선
# problem : https://www.acmicpc.net/problem/17182
# status : solved
# time : 00:14:21
###

N, K = map(int, input().split())
ans = float('inf')

edge = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
  for i in range(N):
    for j in range(N):
      if edge[i][j] > edge[i][k] + edge[k][j] :
        edge[i][j] = edge[i][k] + edge[k][j]

def dfs(node, visited, dist):
  global ans
  if visited == (1 << N) - 1:
    ans = min(ans, dist)
    return

  for i in range(N):
    if visited & (1 << i) : continue
    dfs(i, visited | (1 << i), dist + edge[node][i])

dfs(K, (1 << K), 0)
print(ans)
