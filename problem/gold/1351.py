###
# 1351. 무한 수열
# problem : https://www.acmicpc.net/problem/1351
# status : solved
###

import math
import sys
MAX = int(1e7)
sys.setrecursionlimit(MAX)

N, P, Q = map(int, input().split())
if P < Q : P, Q = Q, P
dp = {}
dp[0] = 1

def solution(n):
  if n < MAX and n in dp:
    return dp[n]
  p, q = math.floor(n/P), math.floor(n/Q)
  dp[p] = solution(p)
  dp[q] = solution(q)
  dp[n] = dp[p]+dp[q]
  return dp[n]

print(solution(N))
