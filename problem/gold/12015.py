###
# 12015. 가장 긴 증가하는 부분 수열 2.
# problem : https://www.acmicpc.net/problem/12015
# status : solved
###
n = int(input())
lst = list(map(int, input().split()))
q = []
  
for i in lst :
  if not q or q[-1] < i :
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
print(len(q))
