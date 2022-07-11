###
# 11812. K진 트리
# problem : https://www.acmicpc.net/problem/11812
# status : solved
# time : ???
###

### trial 1
import sys
input = sys.stdin.readline

N, K, Q = map(int, input().split())
p = lambda x : max(0, (x-1)//K) 
  
for _ in range(Q) :
  a, b = map(int, input().split())
  if K == 1 : 
    print(abs(a-b))
    continue
  a, b = a-1, b-1
  da, db, ta, tb = 0,0,a,b
  while ta != 0 :
    da += 1
    ta = p(ta)
    
  while tb != 0 :
    db += 1
    tb = p(tb)

  if db < da : da, a, db, b = db, b, da, a
  diff = db - da
  cnt = diff
  for _ in range(diff):
    b = p(b)
  
  if a != b :
    cnt += 2
    while p(a) != p(b):
      cnt += 2
      a, b = p(a), p(b)
    
  print(cnt)


### trial 2

import sys
input = sys.stdin.readline

N, K, Q = map(int, input().split())
p = lambda x : max(0, (x-1)//K) 
  
for _ in range(Q) :
  a, b = map(int, input().split())
  if K == 1 : 
    print(abs(a-b))
    continue
  a, b = a-1, b-1
  aa, ab = {a},{b}
  while a != 0 :
    a = p(a)
    aa.add(a)
  while b != 0 :
    b = p(b)
    ab.add(b)
  print(len(aa^ab))
