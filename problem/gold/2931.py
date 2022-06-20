###
# 2931. 가스관
# problem :https://www.acmicpc.net/problem/2931
# status : solved
# time : 00:53:51
###
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

R, C = map(int, input().split())

lst = []
move_dic = {
  '|' : set([0,2]),
  '-' : set([1,3]),
  '+' : set([0,1,2,3]),
  'Z' : set(),
  'M' : set(),
  '1' : set([0,3]),
  '2' : set([2,3]),
  '3' : set([2,1]),
  '4' : set([0,1])
}

for i in range(R):
  tmp = input().strip()
  for j in range(C) :
    if tmp[j] == 'M' :
      M = (j,i)
    if tmp[j] == 'Z' :
      Z = (j,i)
  lst.append(tmp)

def next_move(x, y, d):
  if lst[y][x] == '-' or lst[y][x] == '|' or lst[y][x] == '+':
    return d
  if lst[y][x] == '1':
    return 2 if d == 3 else 1
  if lst[y][x] == '2':
    return 1 if d == 2 else 0
  if lst[y][x] == '3':
    return 3 if d == 2 else 0
  if lst[y][x] == '4' :
    return 3 if d == 0 else 2
  else :
    return d

x, y = M
flg = True
for i in range(4):
  ax, ay = x+dx[i], y+dy[i]
  if -1<ay<R and -1<ax<C and lst[ay][ax] != '.' and i in move_dic[lst[ay][ax]] :
    d = i
    break

while lst[y][x] != '.' :
  x, y = x+dx[d], y+dy[d]
  d = next_move(x,y,d)
  
chk_lst = set()

for i in range(4):
  ax, ay = x+dx[i], y+dy[i]
  if -1<ay<R and -1<ax<C and lst[ay][ax] != '.' and i in move_dic[lst[ay][ax]] :
    chk_lst.add((i-2)%4)

for k, v in move_dic.items() :
  if v == chk_lst :
    print(y+1, x+1, k)
    break
