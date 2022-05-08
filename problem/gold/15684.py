###
# 15684. 사다리 타기
# problem : https://www.acmicpc.net/problem/15684
# status : solved
###

import sys
input = sys.stdin.readline

def move():
  for i in range(N):
    num = i
    for j in range(H):
      if num < N-1 and v[num][j] :
        num += 1
      elif num > 0 and v[num-1][j]:
        num -= 1
    if i != num:
      return False
  return True

def dfs(cnt, idx, r):
  global ans
  if cnt == r :
    if move() :
      print(cnt)
      exit()
    return

  for i in range(idx, H):
    for j in range(N-1):
      if v[j][i] or (j > 0 and v[j-1][i]) or (j < N-2 and v[j+1][i]) : continue
      v[j][i] = True
      dfs(cnt+1, i, r)
      v[j][i] = False

N, M, H = map(int, input().split())
v = [[False]*H for _ in range(N-1)]

for _ in range(M):
  a, b = map(int, input().split())
  v[b-1][a-1] = True

ans = 4
for i in range(4):
  dfs(0,0,i)
print(-1)
    
