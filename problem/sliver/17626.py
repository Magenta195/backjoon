###
# 17626. Four Squares
# problem : https://www.acmicpc.net/problem/17626
# status : solved
###

import sys

n = int(input())
lst = [x**2 for x in range(1, int(n**0.5)+1)]
if n in lst :
  print(1)
else :
  s_lst = [n]
  flg = False
  for i in range(2):
    s_lst = sum([[(y-x) for x in lst] for y in s_lst], [])
    for j in s_lst :
      if j < 0 : continue
      if j in lst:
        print(i+2)
        flg = True
        break
    if flg : break
  if not flg : print(4)
