###
# 17404. RGB거리 2
# problem : https://www.acmicpc.net/problem/17404
# status : solved
###

import sys
input = sys.stdin.readline
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

ans = 1e10
for k in range(3):
  dp = [[1e10]*3 for _ in range(n)]
  for i in range(n):
    if i == 0 : 
      dp[i][k] = lst[i][k]
    elif i == n-1 :
      for j in range(3):
        if j == k : continue
        dp[i][j] = min(dp[i-1][(j+1)%3] + lst[i][j], dp[i-1][(j+2)%3] + lst[i][j])
        ans = min(ans, dp[i][j])
    else :
      for j in range(3):
        dp[i][j] = min(dp[i-1][(j+1)%3] + lst[i][j], dp[i-1][(j+2)%3] + lst[i][j])
        
print(ans)
