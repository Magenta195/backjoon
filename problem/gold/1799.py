###
# 1799. 비숍
# problem : https://www.acmicpc.net/problem/1799
# status : solved
###

### trial 1 (memory 초과) 
dx = [1, 1, -1, -1]
dy = [1, -1, 1, -1]

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
 
q = set()
one_lst = set()

for i in range(n):
  for j in range(n):
    if lst[i][j] == 1 :
      one_lst.add((j,i))
      q.add((j,i,1,()))

o = len(one_lst)
s = 0

while q:
  x, y, cnt, abd_lst = q.pop()
  s = max(s, cnt)
  abd_lst = set(abd_lst)
  abd_lst.add((x,y))
  avail_lst = one_lst - abd_lst
  
  for k in range(4) :
    tx, ty = dx[k], dy[k]
    ax, ay = x + tx, y + ty
    while -1<ax<n and -1<ay<n:
      if (ax,ay) in avail_lst:
        avail_lst.discard((ax,ay))
        abd_lst.add((ax,ay))
      ax, ay = ax + tx, ay + ty

  for ax, ay in avail_lst :
    q.add((ax,ay,cnt+1,tuple(abd_lst)))  

print(s)


### trial 2(시도중)
dx = [1, 1, -1, -1]
dy = [1, -1, 1, -1]

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
 
q = set()
one_lst = set()

for i in range(n):
  for j in range(n):
    if lst[i][j] == 1 :
      one_lst.add((j,i))
      q.add(((j,i),))

s = 0
print(one_lst)
print(q)
while q:
  tup = q.pop()
  s = max(s, len(tup))
  abd_lst = set(tup)
  avail_lst = one_lst - abd_lst

  for ax, ay in avail_lst :
    flg = False
    for k in range(4) :
      tx, ty = dx[k], dy[k]
      tax, tay = ax + tx, ay + ty
      while -1<tax<n and -1<tay<n:
        if (tax,tay) in abd_lst:
          flg = True
          break
        tax, tay = tax + tx, tay + ty
      if flg : break
    if flg : continue
    q.add(tup+((ax,ay),))  

print(s)
