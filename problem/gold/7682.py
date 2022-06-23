###
# 7682. 틱택토
# problem : https://www.acmicpc.net/problem/7682
# status : solved
# time : 00:31:05
###

while True:
  lst = input().strip()
  if lst == 'end' : break

  cx, co = lst.count('X'), lst.count('O')
  if (lst.count('.') > 4 or
      cx-co < 0 or
      cx-co > 1 ):
    print('invalid')
    continue

  O3, X3 = 0, 0

  if lst[0] == lst[4] == lst[8] :
    if lst[4] == 'O' :
      O3 += 1
    elif lst[4] == 'X' :
      X3 += 1
  if lst[2] == lst[4] == lst[6] :
    if lst[4] == 'O' :
      O3 += 1
    elif lst[4] == 'X' :
      X3 += 1
  
  for i in range(3) :
    if lst[i] == lst[i+3] == lst[i+6] :
      if lst[i] == 'O' :
        O3 += 1
      elif lst[i] == 'X' :
        X3 += 1
    if lst[i*3] == lst[i*3+1] == lst[i*3+2] :
      if lst[i*3] == 'O' :
        O3 += 1
      elif lst[i] == 'X' :
        X3 += 1

  if ((O3 > 0 and X3 > 0) or
      O3 == X3 == 0 and lst.count('.') > 0 or
      cx - co == 0 and X3 > 0 or
      cx - co == 1 and O3 > 0) :
    print('invalid')
    continue
  
  print('valid')
