###
# 10830. 행렬 제곱
# problem : https://www.acmicpc.net/problem/10830
# status : solved
###

a, b = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(a)]

def matmul(mat1, mat2) :
  m = [[0]*a for _ in range(a)]
  for i in range(a):
    for j in range(a):
      for k in range(a):
        m[i][j] += mat1[i][k]*mat2[k][j]
      m[i][j] %= 1000
  return m
    
def matpow(mat, n): 
  if n == 1 :
    return mat
  
  pow = matpow(mat, n//2)
  if n%2 == 1 :
    return matmul(matmul(pow, pow), mat)
  else :
    return matmul(pow, pow)
    
mlst = matpow(m, b)
for i in mlst : print(*i)
