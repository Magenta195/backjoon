###
# 11375. 열혈강호
# problem : https://www.acmicpc.net/problem/11375
# status : solved 
# time : 00:16:35
###

N, M = map(int, input().split())
dic = dict()
work = [-1]*(M+1)
for i in range(N):
  cnt, *lst = map(int, input().split())
  dic[i] = lst
  
def dfs(x):
  if visited[x]: return False
  visited[x] = True

  for i in dic[x]:
    if work[i] == -1 or dfs(work[i]):
      work[i] = x
      return True
  return False

ans = 0
for i in range(N):
  visited = [False]*N
  if dfs(i): ans += 1
print(ans)
