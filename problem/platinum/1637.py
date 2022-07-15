###
# 1637. 날카로운 눈
# problem : https://www.acmicpc.net/problem/1637
# status : solved
# time : 00:39:36
###

import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
MAX = 2147483647
start, end = 1, MAX

def count(t):
  cnt = 0
  for a, c, b in lst :
    if a <= t :
      l = min(c, t)
      cnt += (l - a) // b + 1
  return cnt

while start < end :
  mid = (start + end) // 2 
  cnt = count(mid)

  if cnt % 2 == 0 :
    start = mid + 1
  else :
    end = mid

t = count(end)-count(end-1)
if t == 0 :
  print('NOTHING')
else :
  print(end, t)
