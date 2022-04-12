###
# 1029. 그림 교환
# problem : https://www.acmicpc.net/problem/1029
# status : solved
###

import sys
input = sys.stdin.readline

MAX =  10
N = int(input())
lst = [list(input().strip()) for _ in range(N)]
dp = [[[0]*(1<<N+1) for _ in range(N)] for _ in range(MAX)] ## cost, last node, visited

def one_count(st):
  return bin(st).count('1')

def dfs(cost, last_node, visited):
  if dp[cost][last_node][visited] > 0 :
    return dp[cost][last_node][visited]

  cnt = 1
  for k in range(1, N):
    if not visited & (1 << k) and int(lst[last_node][k]) >= cost:
      cnt = max(cnt, 1 + dfs(int(lst[last_node][k]), k, visited | (1 << k)))
  dp[cost][last_node][visited] = cnt
  
  return cnt

print(dfs(0,0,1))
        
    
