###
# 17143. 낚시왕
# problem : https://www.acmicpc.net/problem/17143
# status : solved
###
import sys
input = sys.stdin.readline

rv_dr = [0,2,1,4,3]
R, C, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(M)]
mp = [[-1]*C for _ in range(R)]
for i, l in enumerate(lst):mp[l[0]-1][l[1]-1] = i
score = 0

for i in range(C):
  for j in range(R):
    if mp[j][i] != -1:
      score += lst[mp[j][i]][-1]
      lst[mp[j][i]].clear()
      mp[j][i] = -1
      break
  
  for k, l in enumerate(lst[:]):
    if not l : continue
    oy, ox, spd, dr, sz = l
    mp[oy-1][ox-1] = -1
    mv, axs = (ox-1, C) if dr > 2 else (oy-1, R)
    dr2 = 1 if (dr-2)%4 < 2 else -1

    spd %= 2*(axs-1)
    mv += dr2*spd
    if mv < 0 or mv > axs-1 :
      while mv < 0 or mv > axs-1 :
        dr = rv_dr[dr]
        mv = -mv if mv < 0 else 2*axs - mv - 2
    if mv == 0 or mv == axs-1 : dr = rv_dr[dr]
 
    x, y = (mv, oy-1) if dr > 2 else (ox-1, mv)
    lst[k] = [y+1, x+1, spd, dr, sz]

  for k, l in enumerate(lst[:]):
    if not l : continue
    oy, ox, sz = l[0], l[1], l[4]
    if mp[oy-1][ox-1] > -1 :
      if lst[mp[oy-1][ox-1]][-1] < sz :
        lst[mp[oy-1][ox-1]].clear()
        mp[oy-1][ox-1] = k
      else :
        lst[k].clear()
    else :
      mp[oy-1][ox-1] = k
    
print(score)
