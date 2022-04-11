###
# 1029. 그림 교환
# problem : https://www.acmicpc.net/problem/1029
# status : not solved
###

import sys
input = sys.stdin.readline

MAX =  10
N = int(input())
lst = [list(input().strip()) for _ in range(N)]
dp = [[-1]*N for _ in range(1<<N)]
dp[1][0] = 0

for _ in range(N-1):
  for i in range(N):
    for j in range(1, 1<<N):
      if dp[j][i] > -1: continue
      dp[j][i] = MAX
      for k in range(N):
        if j & (1<<k) and -1 < dp[j - (1<<k)][k] <= int(lst[k][i]):
          dp[j][i] = min(dp[j][i], int(lst[k][i]))
      if dp[j][i] == MAX :
        dp[j][i] = -1

ans = 0
print(dp)
for i in range(N):
  for j in range(1, 1<<N):
    if dp[j][i] < 0 : continue    
    ans = max(ans, bin(j).count('1'))
print(ans)
        
        
    
