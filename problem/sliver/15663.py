###
# 15663. N과 M(9)
# problem : https://www.acmicpc.net/problem/15663
# status : solved
###

n, m = map(int, input().split())
n_lst = sorted(list(map(int, input().split())))
l = len(n_lst)
s = []

def dfs(d):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return
  
  for i in range(d, l):
    if len(s) > 0 :
      if s[-1] >= n_lst[i]:
        continue
    s.append(n_lst[i])
    dfs(i)
    s.pop()

dfs(0)
