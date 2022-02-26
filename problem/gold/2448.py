###
# 2448. 별 찍기 - 11
# problem : https://www.acmicpc.net/problem/2448
# status : solved
###

i = int(input()) // 3
star = ['  *  ',
        ' * * ',
        '*****']

def starmake(lst, n):
  if n == 1 :
    return lst
  
  n_lst = starmake(lst, n//2)
  h = n//2 * 3
  
  return [' '*h + x + ' '*h for x in n_lst] + [x + ' ' + x for x in n_lst]

print(*starmake(star,i), sep='\n')
