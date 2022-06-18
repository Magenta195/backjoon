###
# 13913. 숨바꼭질 4
# problem : https://www.acmicpc.net/problem/13913
# status : solved
# time : 00:07:14
###

from collections import deque

N, K = map(int, input().split())
q = deque([(N,0)])
visited = [-1]*100001
visited[N] = N
rcd = []

while q :
  x, cnt = q.popleft()
  if x == K :
    print(cnt)
    p = x
    rcd.append(p)
    while visited[p] != p :
      rcd.append(visited[p])
      p = visited[p]
    print(*reversed(rcd))
    break

  for ax in [x-1, x+1, 2*x] :
    if -1 < ax < 100001 and visited[ax] == -1 :
      visited[ax] = x
      q.append((ax, cnt+1))
