###
# 21611. 마법사 상어와 파이어볼
# problem : https://www.acmicpc.net/problem/20056
# status : solved(pypy3)
###

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

isdir = lambda x : [0, 2, 4, 6] if sum([y%2 for y in x]) == 0 or sum([y%2 for y in x]) == len(x) else [1, 3, 5, 7]

fireball = []
N, M, K = map(int,input().split())


for i in range(M):
  r, c, m, s, d = map(int,input().split())
  fireball.append([c-1,r-1,m,s,d])

for _ in range(K):
  f_map = [[[] for _ in range(N)] for _ in range(N)]
  for i, (x,y,m,s,d) in enumerate(fireball) :
    fx, fy = (x+dx[d]*s)%N, (y+dy[d]*s)%N
    fireball[i][0], fireball[i][1] = fx, fy
    f_map[fy][fx].append(i)
  del_lst = []
  new = []
  for i in range(N):
    for j in range(N):
      if len(f_map[i][j]) >= 2:
        del_lst.append((j,i))
        nm, ns, dir_lst = 0, 0, []
        for k in f_map[i][j] :
          nm += fireball[k][2]
          ns += fireball[k][3]
          dir_lst.append(fireball[k][4])
        if nm//5 == 0 : continue
        nd = isdir(dir_lst)
        for k in nd :
          new.append([j,i,nm//5, ns//len(f_map[i][j]), k])
  fireball = [x for x in fireball if (x[0], x[1]) not in del_lst] + new

print(sum([x[2] for x in fireball]))
