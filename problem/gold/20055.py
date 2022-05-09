###
# 20055. 컨베이어 벨트
# problem : 
# status : solved
###

from collections import deque
N, K = map(int, input().split())
lst = deque(list(map(int, input().split())))
r_lst = deque([False]*(N))
cnt = 1
while True:
  lst.rotate(1)
  r_lst.rotate(1)
  r_lst[-1] = False
  
  for i in range(N-1,0,-1):
    if not r_lst[i] and r_lst[i-1] and lst[i] > 0 :
      r_lst[i-1], r_lst[i] = False, True
      lst[i] -= 1
  r_lst[-1] = False
  if lst[0] > 0:
    lst[0] -= 1
    r_lst[0] = True
  
  if lst.count(0) >= K : break
  cnt += 1
print(cnt)
