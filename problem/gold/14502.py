###
# 14502. 연구소
# problem : https://www.acmicpc.net/problem/14502
# status : solved
###

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
q = []

s = 0
for i in range(n) :
  for j in range(m):
    if lst[i][j] == 2 :
      q.append((j,i))
    elif lst[i][j] == 0:
      s += 1
s -= 3
m_s = 0

for i in range(n*m):
  if lst[i//m][i%m] > 0 : continue
  for j in range(i+1, n*m):
    if lst[j//m][j%m] > 0 : continue
    for k in range(j+1, n*m):
      if lst[k//m][k%m] > 0 : continue
      t_s = s
      t_q = []
      v = [[True]*m for _ in range(n)]
      for x, y in q:
        v[y][x] = False
        t_q.append((x,y))
      for t in [i, j, k]:
        lst[t//m][t%m] = 1
        v[i//m][i%m] = False
      while t_q:
        x, y = t_q.pop(0)
        for t in range(4):
          ax = x + dx[t]
          ay = y + dy[t]
          if -1<ax<m and -1<ay<n and v[ay][ax] and lst[ay][ax] == 0:
            t_q.append((ax, ay))
            v[ay][ax] = False
            t_s -= 1
      m_s = max(m_s, t_s)
      for t in [i, j, k]:
        lst[t//m][t%m] = 0
print(m_s)
