###
# 20149. 선분 교차 3
# problem : https://www.acmicpc.net/problem/20149
# status : NOT solved
###

def ccw(a, b, c):
  return (a[0]*b[1]+b[0]*c[1]+c[0]*a[1]) - (a[1]*b[0]+b[1]*c[0]+c[1]*a[0])

def check(a, b, c, d)
  c1 = ccw(a,b,c)
  c2 = ccw(a,b,d)
  c3 = ccw(c,d,a)
  c4 = ccw(c,d,b)
  
  if c1*c2 == 0 and c3*c4 == 0:
    if a > b : 
      a,b=b,a
    if c > d :
      c,d=d,c
    if a <= d and c <= b:
      if a == c or b == d :
        return 1
      elif a == d or b == c :
        return (1, a) if a == d else (1, c)
      else : return 1
    else :
      return 0
  elif c1*c2 <= 0 and c3*c4 <= 0:
    m1 = 
    return 1, ((a[0]*
  else : return 0
 
lst = [list(map(int, input().split())) for _ in range(2)]
a, *chk = check(lst[0][:2], lst[0][2:], lst[1][:2], lst[1][2:])
print(a)
if chk : print(*chk)
  
                                              
