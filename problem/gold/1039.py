###
# 1039. 교환
# problem : https://www.acmicpc.net/problem/1039
# status : solved
# time : 00:27:00
###

N, K = input().split()
n, k = len(N), int(K)

q = [(0,N)]
visited = [[False]*k for _ in range(1000001)]
ans = -1
while q :
  cnt, num = q.pop(0)
  if cnt == k :
    ans = max(ans, int(num))
    continue
  for i in range(n-1):
    for j in range(i+1,n):
      if i == 0 and num[j] == '0' : continue
      tmp = list(num)
      tmp[i], tmp[j] = tmp[j], tmp[i]
      tmp = ''.join(tmp)
      if not visited[int(tmp)][cnt] : 
        visited[int(tmp)][cnt] = True
        q.append((cnt+1,tmp))

print(ans)
