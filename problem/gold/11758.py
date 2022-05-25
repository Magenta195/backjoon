###
# 11758. CCW
# problem : https://www.acmicpc.net/problem/11758
# status : solved
# time : 00:03:29
###

def ccw(a, b, c):
  return  (a[1]*b[0]+b[1]*c[0]+c[1]*a[0])-(a[0]*b[1]+b[0]*c[1]+c[0]*a[1])

lst = [list(map(int,input().split())) for _ in range(3)]
i = ccw(lst[0], lst[1], lst[2])
if i < 0 :
  print(1)
elif i > 0 :
  print(-1)
else : print(0)
