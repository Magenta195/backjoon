###
# 1949. 우수 마을
# problem : https://www.acmicpc.net/problem/1949
# status : solved
# time : 00:51:13
###

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
MAX = float('inf')
people = list(map(int, input().split()))
dp = [[0]*3 for _ in range(N)]
edge = { key : [] for key in range(N)}
visited = [False]*N
for _ in range(N-1):
  a, b = map(int, input().split())
  edge[a-1].append(b-1)
  edge[b-1].append(a-1)

def search(node):
  visited[node] = True
  leaf = []
  for next in edge[node]:
    if visited[next] : continue
    leaf.append(next)
    search(next)

  if not leaf:
    dp[node][2] = people[node]
    return dp[node][2]

  min_val = MAX
  dp[node][2] = people[node]
  for next in leaf:
    max_val = max(dp[next][0], dp[next][1])
    if min_val > dp[next][0] - dp[next][2] :
      min_val = dp[next][0] - dp[next][2]
    
    dp[node][2] += max_val
    dp[node][1] += dp[next][0]
    dp[node][0] += max(dp[next][0], dp[next][2])
  if dp[node][1] == dp[node][0] :
    dp[node][0] -= min_val

  return max(dp[node])

print(search(0))
