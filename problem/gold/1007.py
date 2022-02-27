###
# 1007. 벡터 매칭
# problem : https://www.acmicpc.net/problem/1007
# status : 
###
import sys, math
from itertools import combinations
input = sys.stdin.readline

for _ in range(int(input())):
  n = int(input())
  sx, sy = 0, 0
  d = []
  for _ in range(n):
    x, y = map(int, input().split())
    sx += x
    sy += y
    d.append([x,y])
    
  s = 1e10
  f = list(combinations(d, n//2))
  l = len(f)//2
  for lst in f[:l] :
    x, y = 0, 0
    for dx, dy in lst:
      x += dx
      y += dy
    s = min(s, math.sqrt((sx - 2*x)**2 + (sy - 2*y)**2))
  
  print(s)
