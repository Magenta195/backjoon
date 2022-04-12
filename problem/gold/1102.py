###
# 1102. 발전소
# problem : https://www.acmicpc.net/problem/1102
# status : solved
###


### trial 1 (non-DP)
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]

P_lst = input().strip()
P_lst = int(''.join('0' if x == 'N' else '1' for x in P_lst)[::-1], 2)
P = int(input())

dp = [-1]*(1 << N)

def count_one(visited):
  return bin(visited).count('1')

if count_one(P_lst) == 0 :
  print(-1)
else :
  q = [(0, P_lst)]
  while q :
    cost, visited = heappop(q)
    if dp[visited] > -1 : continue
    dp[visited] = cost
    if count_one(visited) >= P:
      print(cost)
      break
    for i in range(N):
      if visited & (1 << i) :
        for j in range(N):
          if not visited & (1 << j):
            new_cost = lst[i][j]
            heappush(q, (cost+new_cost, visited | (1 << j)))
            
### trial 2 (DP)
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]

P_lst = input().strip()[::-1]
P_lst = int(''.join('0' if x == 'N' else '1' for x in P_lst), 2)
P = int(input())
dp = [float('inf')]*(1<<N)
def count_one(visited):
  return bin(visited).count('1')

def dfs(visited, cnt):
  if dp[visited] < float('inf'):
    return dp[visited]

  if cnt >= P:
    return 0

  cost = float('inf')
  for i in range(N):
    if visited & (1 << i) :
      for j in range(N):
        if not visited & (1 << j):
          new_cost = lst[i][j]
          cost = min(cost, new_cost + dfs(visited | (1 << j), cnt+1))
  dp[visited] = cost        
            
  return cost

if count_one(P_lst) >= P :
  print(0)
elif count_one(P_lst) == 0 :
  print(-1)
else :
  print(dfs(P_lst, count_one(P_lst)))
