### 
# 17140. 이차원 배열과 연산
# problem : https://www.acmicpc.net/problem/17140
# status : solved
###

from collections import Counter
r, c, k = map(int,input().split())
lst = [[0]*100 for _ in range(100)]
for i in range(3):
  lst[i][0], lst[i][1], lst[i][2] = map(int,input().split())
if lst[r-1][c-1] == k :
  print(0)
  exit()

row, col = 3, 3
for cnt in range(1, 101) :
  if row >= col :
    new_col = 0
    for i in range(row):
      tmp_lst = sorted(Counter(lst[i]).items(), key=lambda x : (x[0] == 0 ,x[1], x[0]))
      tmp_lst = [x for t in tmp_lst for x in t]
      if tmp_lst[-2] == 0 :
        tmp_lst = tmp_lst[:-2]
      new_col = min(100, max(new_col, len(tmp_lst)))
      if len(tmp_lst) < 100 :
        tmp_lst += [0]*(100 - len(tmp_lst))
      elif len(tmp_lst) > 100 :
        tmp_lst = tmp_lst[:100]
      lst[i] = tmp_lst
    col = new_col
  else :
    new_row = 0
    for i in range(col) :
      tmp_lst = [x[i] for x in lst if x[i] > 0]
      tmp_lst = sorted(Counter(tmp_lst).items(), key=lambda x : (x[0] == 0 ,x[1], x[0]))
      tmp_lst = [x for t in tmp_lst for x in t]
      new_row = min(100, max(new_row, len(tmp_lst)))
      if len(tmp_lst) < 100 :
        tmp_lst += [0]*(100 - len(tmp_lst))
      elif len(tmp_lst) > 100 :
        tmp_lst = tmp_lst[:100]
      for idx, x in enumerate(tmp_lst) :
        lst[idx][i] = x
    row = new_row
  if lst[r-1][c-1] == k :
    print(cnt)
    exit()
print(-1)
    
