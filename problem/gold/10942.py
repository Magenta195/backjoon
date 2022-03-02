###
# 10942. 팰린드롬?
# problem : https://www.acmicpc.net/problem/10942
# status : 
###

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
pal_dp = [[False]*n for _ in range(n)]

for i in range(n):
  pal_dp[i][i] = True
  if i < n-1:
    pal_dp[i][i+1] = lst[i] == lst[i+1]

for i in range(2, n):
  for j in range(n-i):
    pal_dp[j][j+i] = (lst[j] == lst[j+i]) and pal_dp[j+1][j+i-1]
    
for _ in range(int(input())):
  s, e = map(int, input().split())
  print(1 if pal_dp[s-1][e-1] else 0)
