###
# 12100. 2048(easy)
# problem : https://www.acmicpc.net/problem/12100
# status : solved
###

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
from copy import deepcopy

n = int(input())
i_lst = [list(map(int,input().split())) for _ in range(n)]

q = [(i_lst, 0)]

s = 0
while q :
  lst, cnt = q.pop(0)
  for i in range(4):
    a_lst = deepcopy(lst)
    nxt = 1 if i % 2 == 0 else -1
    for j in range(n):
      order = range(1, n) if i % 2 == 0 else range(n-2,-1,-1)
      top = 0 if i % 2 == 0 else n-1
      addable = True      
      for k in order:
        if i < 2 :
          if a_lst[j][k] == 0:
            continue
          if a_lst[j][top] == a_lst[j][k] and addable:
            a_lst[j][k] = 0
            a_lst[j][top] *= 2
            addable = False
          elif a_lst[j][top] == 0:
            a_lst[j][top] = a_lst[j][k]
            a_lst[j][k] = 0
            addable = True
          else :
            if top+nxt != k :
              a_lst[j][top+nxt] = a_lst[j][k]
              a_lst[j][k] = 0
            addable = True
            top += nxt
        else :
          if a_lst[k][j] == 0:
            continue
          if a_lst[top][j] == a_lst[k][j] and addable:
            a_lst[k][j] = 0
            a_lst[top][j] *= 2
            addable = False
          elif a_lst[top][j] == 0:
            a_lst[top][j] = a_lst[k][j]
            a_lst[k][j] = 0
            addable = True
          else :
            if top+nxt != k :
              a_lst[top+nxt][j] = a_lst[k][j]
              a_lst[k][j] = 0
            addable = True
            top += nxt

    if cnt == 4 :
      s = max(s, max(map(max, a_lst)))
    else :
      q.append((a_lst, cnt+1))

print(s)
