###
# 15681. 트리와 쿼리
# problem : https://www.acmicpc.net/problem/15681
# status : solved
# time : 00:08:51
###

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, R, Q = map(int, input().split())

dp = [0]*N
visited = [False]*N
visited[R-1] = True
edge = { key : [] for key in range(N)}

for _ in range(N-1):
  a, b = map(int, input().split())
  edge[a-1].append(b-1)
  edge[b-1].append(a-1)
  
def dfs(node):
  leaf_lst = []
  
  for next in edge[node]:
    if visited[next] : continue
    leaf_lst.append(next)
    visited[next] = True
    dfs(next)
    
  dp[node] = 1
  if not leaf_lst : return
    
  for leaf in leaf_lst :
    dp[node] += dp[leaf]

  return

dfs(R-1)
for _ in range(Q):
  print(dp[int(input())-1])
  
