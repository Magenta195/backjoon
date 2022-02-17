###
# 15652. N과 M(4)
# problem : https://www.acmicpc.net/problem/15652
# status : solved
###

n, m = map(int, input().split())
s = []

def dfs(d):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return
  
  for i in range(d, n+1):
    if len(s) > 0 :
      if s[-1] > i:
        continue
    s.append(i)
    dfs(i)
    s.pop()

dfs(1)
