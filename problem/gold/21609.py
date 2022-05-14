###
# 21609. 상어 중학교
# problem : https://www.acmicpc.net/problem/21609
# status : solved
### 


from collections import deque
import sys
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]


def srt():
  for i in range(N):
    k = 0
    tmp = [lst[j][i] for j in range(N)]
    tmp_lst = [[]]
    for j in range(N):
      if tmp[j] != -1 :
        tmp_lst[k].append(tmp[j])
      else :
        tmp_lst += [[tmp[j]],[]]
        k += 2
    for t in tmp_lst :
      t.sort(key = lambda x : x != -2)
    tmp = [t for tl in tmp_lst for t in tl]
    for j in range(N):
      lst[j][i] = tmp[j]

def rotate():
  global lst
  srt()
  lst = [[lst[j][i] for j in range(N)] for i in range(N-1, -1, -1)]
  srt()

ans = 0
while True:
  visited = [[False]*N for _ in range(N)]
  group = []
  for i in range(N):
    for j in range(N):
      if not visited[i][j] and lst[i][j] > 0:
        visited[i][j] = True
        base = lst[i][j]
        q = deque([(j,i)])
        g = [(j,i,base)]
        cnt = 0
        while q :
          x, y = q.popleft()
          for k in range(4):
            ax, ay = x+dx[k], y+dy[k]
            if -1<ax<N and -1<ay<N and not visited[ay][ax] and lst[ay][ax] in [base, 0] :
              if lst[ay][ax] == 0 :
                cnt += 1
              q.append((ax,ay))
              visited[ay][ax] = True
              g.append((ax,ay,lst[ay][ax]))
        for x, y, base in g :
          if base == 0 : 
            visited[y][x] = False
        if len(g) > 1 :
          g.sort(key = lambda x : (x[2] == 0, x[1], x[0]))
          g.append(cnt)
          group.append(g)
  if not group :
    break
  group = sorted(group, key = lambda x : (-len(x), -x[-1], -x[0][1], -x[0][0]))[0][:-1]
  ans += len(group)**2
  for x, y, _ in group:
    lst[y][x] = -2
  rotate()
print(ans)
