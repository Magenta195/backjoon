###
# 12850. 본대 산책 2
# problem : https://www.acmicpc.net/problem/12850
# status : solved
# 12849. 본대 산책도 같은 풀이로 풀 수 있음
###

init_mat = [
  [0, 1, 1, 0, 0, 0, 0, 0],
  [1, 0, 1, 1, 0, 0, 0, 0],
  [1, 1, 0, 1, 1, 0, 0, 0],
  [0, 1, 1, 0, 1, 1, 0, 0],
  [0, 0, 1, 1, 0, 1, 0, 1],
  [0, 0, 0, 1, 1, 0, 1, 0],
  [0, 0, 0, 0, 0, 1, 0, 1],
  [0, 0, 0, 0, 1, 0, 1, 0]]

def matmul(a, b):
  mat = [[0]*8 for _ in range(8)]
  for i in range(8):
    for j in range(8):
      for k in range(8):
        mat[i][j] += a[i][k]*b[k][j]
      mat[i][j] %= 1000000007
  return mat

def matpow(a, n):
  if n == 1:
    return a
  
  m = matpow(a, n//2)
  m = matmul(m,m)
  if n % 2 == 0:
    return m
  else :
    return matmul(m, a)

num = int(input())
print(matpow(init_mat, num)[0][0])
  
