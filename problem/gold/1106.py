###
# 1106. 호텔
# problem : https://www.acmicpc.net/problem/1106
# status : solved
###

import sys
input = sys.stdin.readline
MAX = int(1e7)
C, N = map(int, input().split())
lst = [[*map(int, input().split())] for _ in range(N)]
dp = [MAX]*(C+1)
dp[0] = 0
  
for i in range(C+1):
  for cost, num in lst :
    result = min(i+num, C)
    dp[result] = min(dp[result], cost + dp[i])

print(dp[C])
