###
# 17779. 개리맨더링 2
# problem :https://www.acmicpc.net/problem/17779
# status : solved
###

N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
MAX = 100*(N**2)
ans = MAX

def solve(x,y,d1,d2):
  tmp = [[False]*N for _ in range(N)]
  R = list(range(d2))+list(range(d2,d2-d1-1,-1))
  L = list(range(0,-d1,-1))+list(range(-d1,d2-d1+1))
  for i, r in enumerate(range(x, x+d1+d2+1)):
    for c in range(y+L[i], y+R[i]+1):
      tmp[r][c] = True
  score = [0]*5
  for r in range(N):
    for c in range(N):
      if tmp[r][c] :
        score[4] += lst[r][c]
      elif r < x+d1 and c <= y :
        score[0] += lst[r][c]
      elif r <= x+d2 and y < c < N :
        score[1] += lst[r][c]
      elif x+d1 <= r < N and c < y-d1+d2 :
        score[2] += lst[r][c]
      else :
        score[3] += lst[r][c]
  return MAX if min(score) == 0 else max(score)-min(score)

for y in range(N):
  for x in range(N):
    for d1 in range(1,N):
      for d2 in range(1,N):
        if x+d1+d2 < N and y >= d1 and y+d2 < N :
          ans = min(ans, solve(x,y,d1,d2))
print(ans)
