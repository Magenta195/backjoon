###
# 11066. 파일 합치기
# problem : https://www.acmicpc.net/problem/11066
# status : solved(pypy3)
# time : ??
###

import sys
input = sys.stdin.readline
MAX = float('inf')
for _ in range(int(input())):
  K = int(input())
  k_lst = list(map(int,input().split()))
  s_lst = [[sum(k_lst[i:j]) if i < j else 0 for j in range(1,K+1)] for i in range(K)]
  dp = [[MAX]*K for _ in range(K)]

  for i in range(K):
    dp[i][i] = 0
  for i in range(1,K):
    for j in range(K-i):
      if i == 1 :
        dp[j][j+i] = k_lst[j] + k_lst[j+i]
      else :
        for k in range(j,j+i):
          dp[j][j+i] = min(dp[j][j+i], dp[j][k]+dp[k+1][j+i])
        dp[j][j+i] += s_lst[j][j+i]
  print(dp[0][-1])
