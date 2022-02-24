###
# 2368. 치즈
# problem : https://www.acmicpc.net/problem/2638
# status : 
###
from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0

while sum(map(sum, lst)) != 0 :
  cnt += 1
  v_v = [[True]*m for _ in range(n)]
  c_v = [[0]*m for _ in range(n)]
  ### 치즈 내부 공간 체크 및 치즈 면적 체크
  for i in range(n) :
    for j in range(m) :
      if lst[i][j] == 0 and v_v[i][j] :
        q = deque([(j,i)])
        v_v[i][j] = False
        tmp = deque([j + i*m])
        
        while q:
          x, y = q.popleft()
          for k in range(4):
            ax = x + dx[k]
            ay = y + dy[k]
            if -1<ax<m and -1<ay<n :
              if lst[ay][ax] == 0 and v_v[ay][ax] :
                tmp.append(ax + ay*m)
                v_v[ay][ax] = False
                q.append((ax, ay))
              elif lst[ay][ax] == 1 :
                c_v[ay][ax] += 1

  ### 만약 닫힌 공간이었다면 치즈 내부 면적을 고려해 빼버리기
        if 0 not in tmp:
          while tmp:
            t = tmp.popleft()
            x, y = t % m, t // m
            for k in range(4):
              ax = x + dx[k]
              ay = y + dy[k]
              if lst[ay][ax] == 1:
                c_v[ay][ax] -= 1
  
  ### 리스트에 최종 반영하기
  for i in range(n) :
    for j in range(m) :
      if c_v[i][j] > 1 : lst[i][j] = 0

print(cnt)
