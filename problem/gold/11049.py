###
# 11049. 행렬 곱셈 순서
# problem : https://www.acmicpc.net/problem/11049
# status : solved (pypy3)
###
import sys
input = sys.stdin.readline
n = int(input())

lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(n) for _ in range(n)]

for i in range(1, n):
  for j in range(n-i):
    x = j+i
    dp[j][x] = 2 ** 32
    for k in range(j, x):
      dp[j][x] = min(dp[j][x], dp[j][k] + dp[k+1][x] + lst[j][0]*lst[k][1]*lst[x][1])

print(dp[0][n-1])  
