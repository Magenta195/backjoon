###
# 9019. DSLR
# problem : https://www.acmicpc.net/problem/9019
# status : solved
# only tested on PyPy3 (not python3)
### 
from collections import deque
import sys

for _ in range(int(sys.stdin.readline())):
  a, b = map(int, sys.stdin.readline().split())
  v = [True]*10000
  v[a] = False
  q = deque([(a,'')])
  
  while q:
    x, cnt = q.popleft()
    if x == b :
      print(cnt)
      break
    for i in ['D','S','L','R']:
      if i == 'D' :
        dx = (2*x) % 10000
      elif i == 'S' :
        dx = x - 1 if x > 0 else 9999
      elif i == 'L' :
        dx = (x % 1000) * 10 + x // 1000
      else :
        dx = (x % 10) * 1000 + x // 10
      if v[dx] :
        v[dx] = False
        q.append((dx, cnt+i))
