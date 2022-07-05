###
# 2213. 트리의 독립집합
# problem : https://www.acmicpc.net/problem/2213
# status : solved
# time : 00:29:59
###

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
dp = [[[0]*2 for _ in range(2)] for _ in range(N)]
edge = {key : [] for key in range(N)}
lst = list(map(int, input().split()))
visited = [False]*N
visited[0] = True

for _ in range(N-1):
  a, b = map(int, input().split())
  edge[a-1].append(b-1)
  edge[b-1].append(a-1)

def dfs(node):
  flg = True
  leaf_lst = []
  for next in edge[node] :
    if visited[next] : continue
    leaf_lst.append(next)
    visited[next] = True
    dfs(next)
    flg = False

  dp[node][1][0] = lst[node]
  dp[node][0][1] = []
  dp[node][1][1] = [node]
  if flg : return
  
  for leaf in leaf_lst :
    dp[node][1][0] += dp[leaf][0][0]
    dp[node][1][1].extend(dp[leaf][0][1])
    
    if dp[leaf][0][0] < dp[leaf][1][0] :
      dp[node][0][0] += dp[leaf][1][0]
      dp[node][0][1].extend(dp[leaf][1][1])
    else :
      dp[node][0][0] += dp[leaf][0][0]
      dp[node][0][1].extend(dp[leaf][0][1])

  return

dfs(0)
if dp[0][0][0] > dp[0][1][0] :
  ans, ans_lst = dp[0][0]
else :
  ans, ans_lst = dp[0][1]

print(ans)
print(*sorted([k+1 for k in ans_lst]))
