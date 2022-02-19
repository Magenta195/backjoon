dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

s, c = 2, 0
step = 0

for j in range(n):
  for i in range(n):
    if lst[j][i] == 9 :
      lst[j][i] = 0
      x = i
      y = j
      break


flg = True
while True:
  q = [(x, y, 0)]
  v = [[True]*n for _ in range(n)]
  v[y][x] = False
  while q:
    _x, _y, cnt = q.pop(0)
    if 0 < lst[_y][_x] < s :
      s, c = s + (c + 1) // s, (c + 1) % s
      x, y = _x, _y
      lst[y][x] = 0
      step += cnt
      flg = False
      break
    for i in range(4):
      ax = _x + dx[i]
      ay = _y + dy[i]
      
      if -1<ax<n and -1<ay<n :
        if v[ay][ax] and lst[ay][ax] <= s:
          v[ay][ax] = False
          q.append((ax, ay, cnt+1))
    q.sort(key=lambda x:(x[2], x[1], x[0]))
    
  if flg :
    print(step)
    break
  flg = True
