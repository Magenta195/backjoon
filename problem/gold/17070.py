###
# 17070.파이프 옮기기 1
# problem : https://www.acmicpc.net/problem/17070
# status : not solved
###

### trial 1

dx = [1, 1, 0]
dy = [0, 1, 1]

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

q = [(1, 0, 0)]
s = 0

while q:
  x, y, a = q.pop(0)
  if x == n-1 and y == n-1 :
    s += 1
    continue
  
  for i in range(3):
    ax = x + dx[i]
    ay = y + dy[i]
    
    if -1<ax<n and -1<ay<n and v[ay][ax] and abs(a - i) <= 1:
      if i != 1 and lst[ay][ax] == 0 :
        q.append((ax, ay, i))
      elif i == 1 and lst[ay][ax] == 0 and lst[y][ax] == 0 and lst[ay][x] == 0 :
        q.append((ax, ay, 1))
print(s)
