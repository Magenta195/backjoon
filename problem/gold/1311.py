###
# 1311. 할 일 정하기 1
# problem : https://www.acmicpc.net/problem/1311
# status : solved(pypy3)
###

import sys

MAX = float('inf')
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
dp = [[MAX]*(1<<N) for _ in range(N)]

def dfs(work, visited):
  if work == N:
    return 0  
  if dp[work][visited] < MAX:
    return dp[work][visited]

  
  tmp = MAX
  for i in range(N):
    if not visited & (1 << i):
      tmp = min(tmp, lst[i][work] + dfs(work + 1, visited | (1 << i)))
  dp[work][visited] = tmp
  return tmp

print(dfs(0,0))
