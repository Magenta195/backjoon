###
# 1528. 금민수의 합
# problem : https://www.acmicpc.net/problem/1528
# status : solved (pypy3)
###

from collections import deque

N = int(input())
gms_lst = []
dp = [-1]*(N+1)

def dfs(n):
  global gms_lst
  for i in [4, 7]:
    num = n*10+i
    if num not in gms_lst and num <= N:
      gms_lst.append(num)
      dfs(num)

dfs(0)
gms_lst.sort()
if not gms_lst : print(-1)
elif gms_lst[-1] == N : print(N)
else :
  q = deque([0])
  while q:
    n = q.popleft()
    for i in gms_lst :
      num = n+i
      if num > N : break
      if dp[num] == -1 :
        if num == N :
          dp[num] = n
          tmp = []
          while num > 0:
            tmp.append(num - dp[num])
            num = dp[num]
          print(*sorted(tmp))
          exit()
        else :
          dp[num] = n
          q.append(num)
  print(-1)
