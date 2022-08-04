###
# 17281. 야구
# problem : https://www.acmicpc.net/problem/17281
# status : solved (pypy3)
# time : 00:41:47
###
import sys
input = sys.stdin.readline

N = int(input())
earning_list = [list(map(int, input().split())) for _ in range(N)]
player_list = [-1]*9
player_list[3] = 0

def play(cnt):
  if cnt < 9 :
    ans = 0
    for i in range(9):
      if player_list[i] == -1 :
        player_list[i] = cnt
        ans = max(ans, play(cnt+1))
        player_list[i] = -1
    return ans

  point = 0
  hitter_num = 0
  for i in range(N):
    f0, f1, f2 = 0, 0, 0
    out = 0
    while out < 3 :
      hitter = player_list[hitter_num]
      hit_result = earning_list[i][hitter]
      if hit_result == 0 :
        out += 1
      elif hit_result == 4:
        point += f0 + f1 + f2 + 1
        f0, f1, f2 = 0, 0, 0
      elif hit_result == 3 :
        point += f0 + f1 + f2
        f0, f1, f2 = 0, 0, 1
      elif hit_result == 2 :
        point += f1 + f2
        f0, f1, f2 = 0, 1, f0
      else :
        point += f2
        f0, f1, f2 = 1, f0, f1
      hitter_num = (hitter_num + 1) % 9
  return point

print(play(1))
