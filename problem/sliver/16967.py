###
# 16967. 배열 복원하기
# problem : https://www.acmicpc.net/problem/16967
# status : solved
# time : 00:19:06
###

H, W, X, Y = map(int, input().split())

B_lst = [list(map(int, input().split())) for _ in range(H+X)]
A_lst = []
for i in range(X):
  A_lst.append(B_lst[i][:W])
for i in range(X, H):
  A_lst.append(B_lst[i][:Y] + [B_lst[i][j]-A_lst[i-X][j-Y] for j in range(Y, W)])

for a in A_lst:print(*a)
