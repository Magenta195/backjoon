###
# 12781. pizza alvoloc
# problem : https://www.acmicpc.net/problem/12781
# status : solved
###

def ccw(ax, ay, bx, by, cx, cy):
  return (ay*bx+by*cx+cy*ax)-(ax*by+bx*cy+cx*ay)

ax, ay, bx, by, cx, cy, dx, dy = map(int, input().split())

c1 = ccw(ax,ay,bx,by,cx,cy)
c2 = ccw(ax,ay,bx,by,dx,dy)
c3 = ccw(cx,cy,dx,dy,ax,ay)
c4 = ccw(cx,cy,dx,dy,bx,by)

print(1 if c1*c2 < 0 and c3*c4 < 0 else 0)
