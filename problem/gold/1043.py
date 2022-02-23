###
# 1043. 거짓말
# problem : https://www.acmicpc.net/problem/1043
# status : solved
###

n, m = map(int, input().split())
t_lst = list(map(int, input().split()))
t_lst.pop(0)
p_lst = [list(map(int, input().split())) for _ in range(m)]

def search(t, f, s, cnt):
  for i in t:
    for j in f:
      if i == j: return 0
  if s == m :
    return cnt
  
  l = 0
  at = t.copy()
  for i in p_lst[s][1:] :
    at.append(i)
  l = max(l, search(list(set(at)), f, s+1, cnt))

  af = f.copy()
  for i in p_lst[s][1:] :
    af.append(i)
  l = max(l, search(t, list(set(af)), s+1, cnt+1))
  return l
print(search(t_lst,[],0, 0))
    
  
  
