###
# 1987. 알파벳
# problem : https://www.acmicpc.net/problem/1987
# status : solved
###
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
R, C = map(int, input().split())
lst = [input().strip() for _ in range(R)]

q = set([(0,0,lst[0][0])])
s = 0

while q :
  x, y, ch = q.pop() 
  s = max(s, len(ch))
  flg = False
  for i in range(4):
    ax = x + dx[i]
    ay = y + dy[i]
    if -1<ax<C and -1<ay<R :
      n_ch = lst[ay][ax]
      if n_ch not in ch:
        q.add((ax,ay, ch+n_ch))
       
print(s)
