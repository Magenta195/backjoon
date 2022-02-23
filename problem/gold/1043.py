###
# 1043. 거짓말
# problem : https://www.acmicpc.net/problem/1043
# status : solved
###

n, m = map(int, input().split())
t, *t_lst = map(int, input().split())
t_lst = set(t_lst)
p_lst = [list(map(int, input().split())) for _ in range(m)]

def search(t, f, s, cnt):
  if t.intersection(f): return 0
  if s == m :
    return cnt
  
  l = 0
  at = t.copy()
  at.update(p_lst[s][1:])
  l = max(l, search(at, f, s+1, cnt))

  af = f.copy()
  af.update(p_lst[s][1:])
  l = max(l, search(t, af, s+1, cnt+1))
  return l
print(search(t_lst,set(),0, 0))
