###
# 14891. 톱니바퀴
# problem : https://www.acmicpc.net/problem/14891
# status : solved
###

from collections import deque

lst = [deque(list(input())) for _ in range(4)]
lst 
K = int(input())
ans = 0
for _ in range(K):
  n, d = map(int, input().split())
  nd, nv = d, lst[n-1][2]
  for i in range(n-1,-1,-1) :
    v = lst[i][-2]
    lst[i].rotate(nd)
    if i > 0 and lst[i-1][2] != v :
      nd = -nd
    else :
      break
  for i in range(n, 4):
    if lst[i][-2] != nv :
      nv = lst[i][2]
      d = -d
      lst[i].rotate(d)
    else :
      break  

print(sum([2**i for i, x in enumerate(lst) if x[0] == '1']))
