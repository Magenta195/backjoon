###
# 2098. 외판원 순회
# problem : https://www.acmicpc.net/problem/2098
# status : solved
###
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[1e10] * (1 << n) for _ in range(n)]

def dfs(x, visited):
  if visited == (1 << n) - 1: 
    if lst[x][0]: return lst[x][0]
    return 1e10

  if dp[x][visited] == -1 :
    return 1e10
  if dp[x][visited] != 1e10:  
    return dp[x][visited]

  for i in range(1, n): 
    if not lst[x][i] or visited & (1 << i):
        continue
    dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << i)) + lst[x][i])
  if dp[x][visited] == 1e10 :
    dp[x][visited] = -1
    return 1e10
  return dp[x][visited]

print(dfs(0, 1))
