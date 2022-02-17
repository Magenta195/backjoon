
###
# 15657. N과 M(8)
# problem : https://www.acmicpc.net/problem/15657
# status : solved
###

n, m = map(int, input().split())
n_lst = sorted(list(map(int, input().split())))
s = []

def dfs(d):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return
  
  for i in range(d, n):
    if len(s) > 0 :
      if s[-1] > n_lst[i]:
        continue
    s.append(n_lst[i])
    dfs(i)
    s.pop()

dfs(0)
