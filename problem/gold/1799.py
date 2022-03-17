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


### trial 2(이분 탐색)
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

dic = { keys : [] for keys in range(2*n-1)}
match = [-1]*(2*n-1)
for i in range(n):
  for j in range(n):
    if lst[i][j] == 1 :
      dic[j+i].append(j-i+n-1)

def dfs(a):
  if visited[a]:
    return False
  visited[a] = True

  for b in dic[a] :
    if match[b] == -1 or dfs(match[b]):
      match[b] = a
      return True
  return False

for i in range(2*n-1):
  visited = [False]*(2*n-1)
  dfs(i)

print(len([i for i in match if i > -1]))
