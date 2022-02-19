###
# 14500. 테트로미노
# problem : https://www.acmicpc.net/problem/14500
# status : solved
### 

import sys

n, m = map(int, sys.stdin.readline().split())
lst = [[x for x in map(int, sys.stdin.readline().split())] for x in range(n)]

s = 0
for y in range(n):
  for x in range(m):
    if x + 3 < m :
      tmp_sum = 0
      for ax in [x + dx for dx in range(4)]:
        tmp_sum += lst[y][ax]
      s = max(tmp_sum, s)
    if y + 3 < n :
      tmp_sum = 0
      for ay in [y + dy for dy in range(4)]:
        tmp_sum += lst[ay][x]
      s = max(tmp_sum, s)

    if x + 1 < m and y + 1 < n :
      tmp_sum = 0
      for ax, ay in [(x + dx, y + dy) for dx, dy in [(0,0),(1,0),(0,1),(1,1)]]:
        tmp_sum += lst[ay][ax]
      s = max(tmp_sum, s)
    
    if x + 2 < m and y + 1 < n :
      tmp_lst = [[r for r in rows[x:x+3]] for rows in lst[y:y+2]]
      tmp_sum = sum(map(sum, tmp_lst))
      s = max(sum(tmp_lst[0]) + max(tmp_lst[1]), sum(tmp_lst[1]) + max(tmp_lst[0]), tmp_sum - min(tmp_lst[0][0]+tmp_lst[-1][-1], tmp_lst[0][-1] + tmp_lst[-1][0]), s)

    if x + 1 < m and y + 2 < n :
      tmp_lst = [[r for r in rows[x:x+2]] for rows in lst[y:y+3]]
      tmp_lst = list(map(list, zip(*tmp_lst)))
      tmp_sum = sum(map(sum, tmp_lst))
      s = max(sum(tmp_lst[0]) + max(tmp_lst[1]), sum(tmp_lst[1]) + max(tmp_lst[0]), tmp_sum - min(tmp_lst[0][0]+tmp_lst[-1][-1], tmp_lst[0][-1] + tmp_lst[-1][0]), s)
 
print(s)
           
