###
# 13460. 구슬 탈출 2
# problem : https://www.acmicpc.net/problem/13460
# status : solved
###
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
lst = [list(input().strip()) for _ in range(n)]
v = [[False]*(m*n) for _ in range(m*n)]


for i in range(n):
  for j in range(m):
    if lst[i][j] == 'B' :
      lst[i][j] = '.'
      B = [j, i]
    elif lst[i][j] == 'R' :
      lst[i][j] = '.'
      R = [j, i]

v[R[1]*m+R[0]][B[1]*m+B[0]] = True

q = []
q.append([R, B, 0])

def move(x, y, l):
  ax = x + dx[l]
  ay = y + dy[l]
  while lst[ay][ax] != '#' :
    if lst[ay][ax] == 'O' :
      return ax, ay, True
    elif [ax, ay] in [aR,aB]:
      break
    ax += dx[l]
    ay += dy[l]
    
  return ax-dx[l], ay-dy[l], False
    
flg = False
while q :
  R, B, cnt = q.pop(0)
  for i in range(4):
    aR = R.copy()
    aB = B.copy()
    j = 0 if i < 2 else 1
    func = min if i % 2 == 0 else max
    RBchk = aR[j] == func(aR[j], aB[j])
    f_move = aR if RBchk else aB
    s_move = aB if RBchk else aR
    
    f_move[0], f_move[1], F_chk = move(f_move[0], f_move[1], i)
    s_move[0], s_move[1], S_chk = move(s_move[0], s_move[1], i)
    
    if v[aR[1]*m+aR[0]][aB[1]*m+aB[0]] or cnt > 9 : continue
    if (RBchk and S_chk) or (not RBchk and F_chk) : continue
    elif (RBchk and F_chk) or (not RBchk and S_chk) :
      print(cnt+1)
      flg = True
      break
    else :
      v[aR[1]*m+aR[0]][aB[1]*m+aB[0]] = True
      q.append([aR, aB, cnt+1])
  if flg : break
if not flg : print(-1)
