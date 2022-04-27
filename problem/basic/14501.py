###
# 14501. 퇴사
# problem : https://www.acmicpc.net/problem/14501
# status : solved
###

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

def dfs(now):
  if now >= N :
    return 0
  val = 0
  for i in range(now, N):
    if i+lst[i][0] <= N :
      val = max(val, lst[i][1]+dfs(i+lst[i][0]))
  return val

print(dfs(0))
