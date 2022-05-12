###
# 19236. 청소년 상어
# problem : https://www.acmicpc.net/problem/19236
# status : solved
###


dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

fish = [-1]*16
room = [[-1]*4 for _ in range(4)]
for i in range(4):
  lst = list(map(int,input().split()))
  for j in range(4):
    fish[lst[j*2]-1] = (j, i, lst[j*2+1]-1)
    room[i][j] = lst[j*2]-1

init = room[0][0]
shark = fish[init]
room[0][0], fish[init] = -1, -1
ans = init+1

def dfs(f_lst, s_lst, r_lst, val):
  sx, sy, sdir = s_lst
  tf_lst = f_lst[:]
  tr_lst = [t[:] for t in r_lst]
  
  for i in range(16):
    if tf_lst[i] != -1 :
      flg = False
      x, y, dir = tf_lst[i]
      for j in range(8):
        adir = (dir+j)%8
        ax, ay = x + dx[adir], y + dy[adir]
        if -1 < ax < 4 and -1 < ay < 4 and (ax, ay) != (sx, sy) :
          flg = True
          break
      if flg :
        tf_lst[i] = (ax, ay, adir)
        if tr_lst[ay][ax] != -1 :
          _, _, bdir = tf_lst[tr_lst[ay][ax]]
          tf_lst[tr_lst[ay][ax]] = (x, y, bdir)
        tr_lst[ay][ax], tr_lst[y][x] = tr_lst[y][x], tr_lst[ay][ax]

  tmp = val
  while -1 < sx < 4 and -1 < sy < 4 :
    sx += dx[sdir]
    sy += dy[sdir]
    if -1 < sx < 4 and -1 < sy < 4 and tr_lst[sy][sx] > -1 :
      victim = tr_lst[sy][sx]
      new_s = tf_lst[victim]
      tr_lst[sy][sx], tf_lst[victim] = -1, -1
      tmp = max(tmp, dfs(tf_lst, new_s, tr_lst, val+victim+1))
      tr_lst[sy][sx], tf_lst[victim] = victim, new_s
  return tmp
  
print(dfs(fish, shark, room, init+1))
