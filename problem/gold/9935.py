###
# 9935. 문자열 폭발
# problem : https://www.acmicpc.net/problem/9935
# status : solved
###

# trial (official, solved)
s = input().strip()
b = input().strip()
stk = []

for i in s:
  stk.append(i)
  if i == b[-1] and len(stk) >= len(b):
    if ''.join(stk[-len(b):]) == b :
      del stk[-len(b):]

print('FRULA' if len(stk) == 0 else ''.join(stk)) 

# trial 예외로 한 번 도전해봄 (시간 초과)
s = input().strip()
b = input().strip()
n_s = ''.join(s.split(b))

while n_s != s :
  s = n_s
  n_s = ''.join(s.split(b))

print('FRULA' if len(s) == 0 else s) 
