###
# 14616. Explore space
# problem : https://www.acmicpc.net/problem/14616
# status : solved
###
import sys
input = sys.stdin.readline

n = int(input())
r_lst = [list(map(int, input().split())) for _ in range(n)]
for i in range(n) :
  if r_lst[i][1] * r_lst[i][2] < r_lst[i][0] * r_lst[i][3] :
    r_lst[i][0], r_lst[i][1], r_lst[i][2], r_lst[i][3] = r_lst[i][2], r_lst[i][3], r_lst[i][0], r_lst[i][1]
m = int(input())
m_lst = sorted([list(map(int, input().split())) for _ in range(m)], key = lambda x : (x[1]/x[0]))
cnt = 0
for x1, y1, x2, y2 in r_lst:
  start, end = 0, m-1
  while start <= end:
    mid = (start + end) // 2
    mx, my = m_lst[mid]
    if y1/x1 >= my/mx >= y2/x2 :
      cnt += 1
      break
    elif my/mx < y2/x2 : start = mid + 1
    else : end = mid - 1
  
print(n - cnt)
