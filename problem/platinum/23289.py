###
# 23289. 온풍기 안녕!
# problem : https://www.acmicpc.net/problem/23289
# status : solved
# time : 01:54:29
###

R, C, K = map(int, input().split())
dr, dc, oth = [0, 0, -1, 1],[1, -1, 0, 0],[1, 0, 3, 2]
hmap = [[0]*C for _ in range(R)]
heater = [[] for _ in range(4)]
chk = []

for i in range(R):
  lst = list(map(int,input().split()))
  for j in range(C):
    if lst[j] == 5:
      chk.append((i,j))
    elif lst[j] > 0:
      heater[lst[j]-1].append((i,j))

W = int(input())
w_lst = [[[False]*4 for _ in range(C+1)] for _ in range(R+1)]
for _ in range(W):
  x,y,t = map(int, input().split())
  if t==0 : w_lst[x-2][y-1][3] = w_lst[x-1][y-1][2] = True  
  else : w_lst[x-1][y-1][0] = w_lst[x-1][y][1] = True

for i, h in enumerate(heater):
  for j in h :
    r, c = j
    orth = (i-2)%4
    h_lst = set([(r+dr[i],c+dc[i],5)])
    lst = set([(r+dr[i],c+dc[i])])
    for k in range(4,0,-1):
      next_lst = set() 
      for l in lst :
        ar,ac = l[0]+dr[i], l[1]+dc[i]
        ur,uc,lr,lc = l[0]+dr[orth],l[1]+dc[orth],l[0]+dr[oth[orth]],l[1]+dc[oth[orth]]
        uar,uac,lar,lac = ar+dr[orth],ac+dc[orth],ar+dr[oth[orth]],ac+dc[oth[orth]]
        if -1 < ar < R and -1 < ac < C and not w_lst[ar][ac][oth[i]] :
          next_lst.add((ar, ac))
          h_lst.add((ar,ac,k))
        if -1 < uar < R and -1 < uac < C and not w_lst[ur][uc][oth[orth]] and not w_lst[ur][uc][i]:
          next_lst.add((uar, uac))
          h_lst.add((uar,uac,k))
        if -1 < lar < R and -1 < lac < C and not w_lst[lr][lc][orth] and not w_lst[lr][lc][i]:
          next_lst.add((lar, lac))
          h_lst.add((lar,lac,k))
      lst = next_lst
    for r, c, k in h_lst :
      if r < R and c < C:
        hmap[r][c] += k
        
total_h = [[0]*C for _ in range(R)]
for i in range(1, 101):
  for r in range(R):
    for c in range(C):
      total_h[r][c] += hmap[r][c]
  next_h = [[0]*C for _ in range(R)]
  for r in range(R):
    for c in range(C):
      if r in [0, R-1] or c in [0, C-1] : next_h[r][c] -= 1
      for j in [0,3]:
        ar, ac = r+dr[j], c+dc[j]
        if ar < R and ac < C and not w_lst[r][c][j]:
          t = total_h[r][c] - total_h[ar][ac]
          d = 1 if t > 0 else -1
          t = d*(abs(t)//4)
          if t != 0 :
            next_h[r][c] -= t
            next_h[ar][ac] += t
  for r in range(R):
    for c in range(C):
      total_h[r][c] = max(0, total_h[r][c]+next_h[r][c])
  if sum([total_h[r][c] >= K for (r,c) in chk]) == len(chk) :
    print(i)
    exit()
print(101)
