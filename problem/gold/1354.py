###
# 1354. 무한 수열 2
# problem : https://www.acmicpc.net/problem/1354
# status : solved
###

import math
import sys
MAX = int(1e7)
sys.setrecursionlimit(MAX)

N, P, Q, X, Y = map(int, input().split())
dp = {}
dp[0] = 1

def solution(n):
  if n < MAX and n in dp:
    return dp[n]
  p = max(math.floor(n/P) - X, 0)
  q = max(math.floor(n/Q) - Y, 0)
  dp[p] = solution(p)
  dp[q] = solution(q)
  dp[n] = dp[p]+dp[q]
  return dp[n]

print(solution(N))
