###
# 15666. N과 M(12)
# problem : https://www.acmicpc.net/problem/15666
# status : solved
###

n, m = map(int, input().split())
n_lst = sorted(list(set(map(int, input().split()))))
l = len(n_lst)
s = []

def dfs(d):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return
  
  for i in range(d, l):
    s.append(n_lst[i])
    dfs(i)
    s.pop()

dfs(0)
