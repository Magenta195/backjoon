###
# 17317. 이사
# problem : https://www.acmicpc.net/problem/17371
# status : solved
###
import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

l = 1e10
mx, my = -1, -1
for i in range(n):
  x, y = lst[i]
  n_l = 0
  for j in range(n):
    ax, ay = lst[j]
    nn_l = (x-ax)**2 + (y-ay)**2
    if nn_l > n_l :
      n_l = nn_l
  if n_l < l :
    l = n_l
    mx,my = x,y

print(mx, my)
