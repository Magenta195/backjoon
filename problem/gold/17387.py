###
# 17387. 선분 교차
# problem : https://www.acmicpc.net/problem/17387
# status : solved
###
def ccw(ax, bx, cx, ay, by, cy):
  return (ax*by + bx*cy + cx*ay) - (bx*ay + cx*by + ax*cy)

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

c1 = ccw(x1, x2, x3, y1, y2, y3)
c2 = ccw(x1, x2, x4, y1, y2, y4)
c3 = ccw(x3, x4, x1, y3, y4, y1)
c4 = ccw(x3, x4, x2, y3, y4, y2)

if c1*c2 == 0 and c3*c4 == 0 :
  print(1 if (
    max(x1,x2) >= min(x3,x4) and 
    max(x3,x4) >= min(x1,x2) and 
    max(y1,y2) >= min(y3,y4) and
    max(y3,y4) >= min(y1,y2)) else 0)
elif c1*c2 <= 0 and c3*c4 <= 0 : print(1)
else : print(0)
