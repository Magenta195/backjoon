###
# 12886. 돌 그룹
# problem : https://www.acmicpc.net/problem/12886
# status : solved
# time : 00:12:47
###
A,B,C = map(int,input().split())
M = A+B+C

def srt(A,B):
  a, b = A*2, B-A
  if a > b : a,b=b,a
  return [a,b]
if M % 3 == 0 :
  visited = [[False]*M for _ in range(M)]
  A,B,C = sorted([A,B,C])
  visited[A][B] = True
  q = [[A,B,C]]
  while q :
    A,B,C = q.pop()
    if A == B == C:
      print(1)
      exit()
    for x,y,z in [(A,B,C),(B,C,A),(A,C,B)]:
      if x < y :
        x,y,z = sorted(srt(x,y)+[z])
        if not visited[x][y] :
          visited[x][y] = True
          q.append([x,y,z])
print(0)
