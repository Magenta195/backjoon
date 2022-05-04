###
# 17825. 주사위 윷놀이
# problem : https://www.acmicpc.net/problem/17825
# status : solved
###

board = [[0,
         2, 4, 6, 8, 10,
         12, 14, 16, 18, 20,
         22, 24, 26, 28, 30,
         32, 34, 36, 38, 40],
         [10, 13, 16, 19, 25],
         [20, 22, 24, 25],
         [30, 28, 27, 26, 25],
         [25, 30, 35, 40],
         [40, 0]]
board_max = [20, 4, 3, 4, 3, 1]
ans = 0

def solve(now, horse, val):
  global ans
  if now == 10 :
    ans = max(ans, val)
    return 
  
  dice = lst[now]
  for i in range(4):
    bd, num = horse[i]
    if num == board_max[bd] : continue
    num += dice
    if bd == 0 and num in [5, 10, 15] :
      bd, num = num//5, 0
    if 1 <= bd <= 3 and num >= board_max[bd] :
      bd, num = 4, num - board_max[bd]
    if (bd == 0 or bd == 4) and num >= board_max[bd] :
      bd, num = 5, num - board_max[bd]
    num = min(num, board_max[bd])
    if num != board_max[bd] and (bd, num) in horse :
      continue
    next_horse = horse[:]
    next_horse[i] = (bd,num)
    solve(now+1, next_horse, val + board[bd][num])

lst = list(map(int, input().split()))
solve(0,[(0,0)]*4,0)
print(ans)


  
