###
# 2568. 전깃줄 - 2
# problem : https://www.acmicpc.net/problem/2568
# status : solved
###
import sys
input = sys.stdin.readline
n = int(input())
lst = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x:x[0])
b_lst = [x for _, x in lst]
q = []
rcd = []
g = { k : v for v, k in lst }

for b in b_lst :
  if not q or q[-1] < b :
    rcd.append((len(q), b))
    q.append(b)
    continue
  start, end = 0, len(q)-1
  while start < end:
    mid = (start + end)//2
    if q[mid] < b:
      start = mid + 1
    else :
      end = mid
  q[end] = b
  rcd.append((end, b))

cnt = len(q)-1
print(n - cnt - 1)
for i, num in reversed(rcd):
  if i == cnt :
    cnt -= 1
    del g[num]
  if cnt < 0 : break

print(*sorted(g.values()), sep='\n')

### 2565. 전깃줄 역시 백트레킹 부분만 제외하면 동일

###
# 2565. 전깃줄
# problem : https://www.acmicpc.net/problem/2565
# status : solved
###

import sys
input = sys.stdin.readline
n = int(input())
lst = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x:x[0])
b_lst = [x for _, x in lst]
q = []

for b in b_lst :
  if not q or q[-1] < b :
    q.append(b)
    continue
  start, end = 0, len(q)-1
  while start < end:
    mid = (start + end)//2
    if q[mid] < b:
      start = mid + 1
    else :
      end = mid
  q[end] = b

print(n - len(q))
