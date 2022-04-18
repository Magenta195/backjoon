###
# 1103. 게임
# problem : https://www.acmicpc.net/problem/1103
# status : solved
###

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
lst = [input().strip() for _ in range(N)]
visited = [[False]*M for _ in range(N)]
visited[0][0] = True
dp = [[0]*M for _ in range(N)]
ans = 0

def dfs(x, y, cnt):
  global ans
  dp[y][x] = cnt
  ans = max(cnt, ans)
  mul = int(lst[y][x])
  for i in range(4):
    ax = x + dx[i] * mul
    ay = y + dy[i] * mul
    if -1 < ax < M and -1 < ay < N and lst[ay][ax] != 'H' and cnt+1 > dp[ay][ax]:
      if visited[ay][ax] :
        print(-1)
        exit()
      visited[ay][ax] = True
      dfs(ax, ay, cnt+1)
      visited[ay][ax] = False

dfs(0,0,0)
print(ans+1)
