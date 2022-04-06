###
# 1708. 볼록 껍질
# problem : https://www.acmicpc.net/problem/1708
# status : solved
###

import sys
from collections import deque
from functools import cmp_to_key

def ccw(a, b, c):
  return (a[0]*b[1] + b[0]*c[1] + c[0]*a[1]) - (a[1]*b[0] + b[1]*c[0] + c[1]*a[0])

def dis(a,b):
  return (a[0]-b[0])**2 + (a[1]-b[1])**2

def ccw_compare(x,y):
  if ccw(lst[0],x,y) < 0 :
    return 1
  elif ccw(lst[0],x,y) == 0:
    return 0
  else : return -1

input = sys.stdin.readline
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key = lambda x : (x[1], x[0]))
lst[1:] = sorted(lst[1:], key = cmp_to_key(ccw_compare))
stk = deque([])
stk += lst[:2]
i = 2
while i < N :
  c = ccw(stk[-2], stk[-1], lst[i])
  if c > 0 :
    stk.append(lst[i])
    i += 1
  elif c == 0:
    tmp = stk.pop()
    tmp = lst[i] if dis(stk[-1], tmp) < dis(stk[-1], lst[i]) else tmp
    stk.append(tmp)
    i += 1
  else :
    stk.pop()

print(len(stk))
