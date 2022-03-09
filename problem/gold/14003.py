###
# 14003. 가장 긴 증가하는 부분 수열 5
# problem : https://www.acmicpc.net/problem/14003
# status : solved
###

n = int(input())
lst = list(map(int, input().split()))
q = []
rcd = []

for i in lst :
  if not q or q[-1] < i :
    rcd.append((len(q), i))
    q.append(i)
  else :
    start, end = 0, len(q)-1
    while start < end :
      mid = (start + end) // 2
      if i > q[mid] :
        start = mid + 1
      else :
        end = mid
    q[end] = i
    rcd.append((end, i))  

k = len(q)
dq = []
print(k)
for i, num in reversed(rcd):
  if i == k :
    k -= 1
    dq.append(num)
  if k < 0 : break
print(*reversed(dq))
    
