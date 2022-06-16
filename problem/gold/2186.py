###
# 2186. 문자판
# problem : https://www.acmicpc.net/problem/2186
# status : solved
###

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
dx = [i*k for i in [0, 0, -1, 1] for k in range(1,K+1)]
dy = [i*k for i in [-1, 1, 0, 0] for k in range(1,K+1)]

lst = [input().strip() for _ in range(N)]
word = input().strip()
dp = [[[-1]*M for _ in range(N)] for _ in range(len(word))]
ans = 0

def dfs(x, y, cnt):
  global ans
  if cnt == len(word) :
    return 1

  if dp[cnt][y][x] > -1 :
    return dp[cnt][y][x]

  dp[cnt][y][x] = 0
  for i in range(4*K):
    ax, ay = x+dx[i], y+dy[i]
    if -1<ax<M and -1<ay<N and word[cnt] == lst[ay][ax] :
      dp[cnt][y][x] += dfs(ax, ay, cnt+1)
  return dp[cnt][y][x]
 
for i in range(N):
  for j in range(M):
    if lst[i][j] == word[0]:
      ans += dfs(j,i,1)

print(ans)
