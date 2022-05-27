###
# 17386. 선분 교차 1
# problem : https://www.acmicpc.net/problem/17386
# status : solved
# time : 00:07:46
###
def ccw(ax, ay, bx, by, cx, cy):
  return (ay*bx+by*cx+cy*ax)-(ax*by+bx*cy+cx*ay)

def solve():
  ax,ay,bx,by = map(int,input().split())
  cx,cy,dx,dy = map(int,input().split())
  c1,c2 = ccw(ax,ay,bx,by,cx,cy),ccw(ax,ay,bx,by,dx,dy)
  c3,c4 = ccw(cx,cy,dx,dy,ax,ay),ccw(cx,cy,dx,dy,bx,by) 
  print(1 if c1*c2 < 0 and c3*c4 < 0 else 0)

solve()
