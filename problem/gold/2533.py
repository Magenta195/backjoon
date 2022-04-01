###
# 2533. 사회망 서비스(SNS)
# problem : https://www.acmicpc.net/problem/2533
# status : solved
###

import sys
sys.setrecursionlimit(int(1e7))
input = sys.stdin.readline
N = int(input())
lst = [[] for _ in range(N+1)]
dp = [[0,0] for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(N-1):
  a, b = map(int,input().split())
  lst[a].append(b)
  lst[b].append(a)
  
def dfs(node):
  visited[node] = True
  dp[node][0] = 0
  dp[node][1] = 1
  for i in lst[node]:
    if not visited[i]:
      dfs(i)
      dp[node][0] += dp[i][1]
      dp[node][1] += min(dp[i][0], dp[i][1])
 
dfs(1)
print(min(dp[1]))
      
  
