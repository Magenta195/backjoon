###
# 1082. 방 번호
# problem : https://www.acmicpc.net/problem/1082
# status : solved
###

import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
M = int(input())

dp = [[0]*(N+1) for _ in range(M+1)]

def largest_num(lst):
  result = ''
  for i in range(N-1,-1,-1):
    result += str(i)*lst[i]
  return int(result)
    
for i in range(N):
  if P[i] <= M :
    dp[P[i]][i] += 1
    dp[P[i]][i] = i
    
for i in range(M):
  for j in range(N):
    if i + P[j] <= M :
      tmp = dp[i][:-1]
      tmp[j] += 1
      result = largest_num(tmp)
      if result > dp[i+P[j]][-1] :
        dp[i+P[j]] = tmp
        dp[i+P[j]].append(result)

ans = 0
for i in range(M+1):
  ans = max(ans, dp[i][-1])
print(ans)
