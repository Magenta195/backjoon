###
# 16953. A -> B
# problem : https://www.acmicpc.net/problem/16953
# status : solved
###

a, b = map(int, input().split())
q = [(a, 0)]
flg = True
while q:
  x, cnt = q.pop(0)
  if x == b :
    flg = False
    print(cnt+1)
    break
  
  for i in [x*2, 10*x + 1] :
    if i <= b : q.append((i, cnt+1))
if flg : print(-1)
  
###
# note : 맨 처음엔 visited를 표기하려고 v 리스트를 추가했는데... 이것 때문에 메모리 초과 오류가 났다. 사실 본 문제는 10^9까지 배열이 커질 수 있으므로 약간의
# 비효율을 감수하고서라도 리스트를 표기할 필요가 없다.
###
