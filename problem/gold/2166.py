###
# 2166. 다각형의 면적
# problem : https://www.acmicpc.net/problem/2166
# status : solved
###

import sys

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.append(lst[0])
s = 0
for i in range(n):
  s += lst[i][0]*lst[i+1][1] - lst[i][1]*lst[i+1][0]
print('{:0.1f}'.format(abs(s)/2))
