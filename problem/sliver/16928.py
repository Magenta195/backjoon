###
# 16928. 뱀과 사다리 게임
# problem : https://www.acmicpc.net/problem/16928
# status : solved
###
import sys

n, m = map(int, sys.stdin.readline().split())
lst = [[x for x in map(int, sys.stdin.readline().split())] for _ in range(n+m)]
chk = [x[0] for x in lst]
v = [0]*101
q = [(1,0)]

while q:
  x, cnt = q.pop(0)
  if v[x] > 0 : continue
  v[x] += 1
  for i in range(1,7):
    if x+i > 100: break
    elif x+i == 100:
      print(cnt+1)
      q = []
      break
    else:
      q.append((lst[chk.index(x+i)][1], cnt+1) if x+i in chk else (x+i, cnt+1))
      
    



