###
# 20061. 모노미노도미노2
# problem : https://www.acmicpc.net/problem/20061
# status : solved
# time : 00:38:49
###

d_brd = [[0]*4 for _ in range(10)]
r_brd = [[0]*4 for _ in range(10)]

N = int(input())
score = 0
for _ in range(N):
  t, y, x = map(int, input().split())
  if t == 1 :
    dd = [(x,y)]
    rd = [(3-y,x)]
  elif t == 2 :
    dd = [(x,y),(x+1,y)]
    rd = [(3-y,x),(3-y,x+1)]
  else :
    dd = [(x,y),(x,y+1)]
    rd = [(3-y,x),(2-y,x)]

  while True:
    tmp = []
    for x,y in rd :
      y += 1
      if y > 9 or r_brd[y][x] : break
      tmp.append((x,y))
    if y > 9 or r_brd[y][x] : 
      for x,y in rd :
        r_brd[y][x] = 1
      break
    else : rd = tmp
  while True:
    tmp = []
    for x,y in dd :
      y += 1
      if y > 9 or d_brd[y][x] : break
      tmp.append((x,y))
    if y > 9 or d_brd[y][x] :
      for x,y in dd :
        d_brd[y][x] = 1
      break
    else : dd = tmp
    
  for y in range(6,10):
    if sum(r_brd[y]) == 4 :
      score += 1
      r_brd[y] = [0]*4
    if sum(d_brd[y]) == 4:
      score += 1
      d_brd[y] = [0]*4
  r_brd.sort(key = lambda x : sum(x) !=0)
  d_brd.sort(key = lambda x : sum(x) !=0)
  r_cnt, d_cnt = 0,0
  for y in range(4,6):
    if sum(r_brd[y]) > 0 :
      r_cnt += 1
    if sum(d_brd[y]) > 0 :
      d_cnt += 1
  for _ in range(r_cnt) :
    del r_brd[-1]
    r_brd = [[0]*4] + r_brd
  for _ in range(d_cnt) :
    del d_brd[-1]
    d_brd = [[0]*4] + d_brd

print(score, sum(map(sum, r_brd+d_brd)), sep='\n')
