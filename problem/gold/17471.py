###
# 17471. 게리멘더링
# problem : https://www.acmicpc.net/problem/17471
# status : solved
# time : 00:17:38
###

from itertools import combinations

N = int(input())
people_num = list(map(int, input().split()))
edge = {}

for i in range(1,N+1):
  p_num, *lst = map(int, input().split())
  edge[i] = lst

ans = float('inf')
for i in range(1, N//2+1):
  for a_list in combinations(range(1,N+1), i) :
    b_list = [i for i in range(1,N+1) if i not in a_list]
    a_visited = { key : False for key in a_list}
    b_visited = { key : False for key in b_list}
    a_visited[a_list[0]] = b_visited[b_list[0]] = True
    a_q = [a_list[0]]
    b_q = [b_list[0]]
    a_cnt = b_cnt = 0
    while a_q :
      node = a_q.pop()
      a_cnt += people_num[node-1]
      for next in edge[node]:
        if next in a_visited and not a_visited[next] :
          a_visited[next] = True
          a_q.append(next)
    if False in a_visited.values() : continue
    while b_q :
      node = b_q.pop()
      b_cnt += people_num[node-1]
      for next in edge[node]:
        if next in b_visited and not b_visited[next] :
          b_visited[next] = True
          b_q.append(next)
    if False in b_visited.values() : continue
    ans = min(ans, abs(a_cnt-b_cnt))

print(ans if ans < float('inf') else -1)
