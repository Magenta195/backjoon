###
# 10830. 행렬 제곱
# problem : https://www.acmicpc.net/problem/10830
# status : solved
###

def matmul(mat, n):
  if n == 1 :
    return mat
  if n == 2 :
    m = [[0]*n for _ in range(n)]
    for i in range(n):
      for j in range(m):
        m[i][j] = sum([x*y for x, y in zip(mat[i]
