###
# 5022. 연결
# problem : https://www.acmicpc.net/problem/5022
# status : solved
# time : 00:26:18
###

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, M = map(int, input().split())
A1, A2, B1, B2 = (tuple(map(int, input().split())) for _ in range(4))
MAX = float('inf')
ans = MAX
for fs, fe, ss, se in [[A1,A2,B1,B2], [B1,B2,A1,A2]]:
  visited = [[(-1,-1)]*(N+1) for _ in range(M+1)]
  fx, fy = fs
  visited[fy][fx] = (fx, fy)
  q = [(fx,fy,0)]
  tmp1, tmp2 = MAX, MAX
  while q :
    fx, fy, cnt = q.pop(0)
    if (fx,fy) == fe :
      tmp1 = cnt
      break
    for i in range(4):
      ax, ay = fx+dx[i], fy+dy[i]
      if -1 < ax < N+1 and -1 < ay < M+1 and visited[ay][ax] == (-1,-1) and (ax, ay) != ss and (ax, ay) != se:
        visited[ay][ax] = (fx,fy)
        q.append((ax,ay,cnt+1))

  s_visited = [[(-1,-1)]*(N+1) for _ in range(M+1)]
  (ax, ay), (sx, sy) = fe, ss
  s_visited[ay][ax] = visited[ay][ax]
  s_visited[sy][sx] = (sx,sy)
  while (ax, ay) != fs :
    ax, ay = visited[ay][ax]
    s_visited[ay][ax] = visited[ay][ax]

  q = [(sx,sy,0)]
  while q:
    sx, sy, cnt = q.pop(0)
    if (sx,sy) == se :
      tmp2 = cnt
      break
    for i in range(4):
      ax, ay = sx+dx[i], sy+dy[i]
      if -1 < ax < N+1 and -1 < ay < M+1 and s_visited[ay][ax] == (-1,-1) :
        s_visited[ay][ax] = (sx,sy)
        q.append((ax,ay,cnt+1))

  if tmp1 < MAX and tmp2 < MAX : ans = min(ans, tmp1+tmp2)
print(ans if ans < MAX else 'IMPOSSIBLE')
