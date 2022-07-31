###
# 17136. 색종이 붙이기
# problem : https://www.acmicpc.net/problem/17136
# status : solved(pypy3)
###

paper_list = [list(map(int, input().split())) for _ in range(10)]
answer = 26
enabled_papers = [5]*5
left_ones = sum(map(sum, paper_list))
visited = [[[0]*left_ones for _ in range(25)] for _ in range(100)]

def check(x,y,width):
  for wy in range(y,y+width+1):
    for wx in range(x,x+width+1):
      if paper_list[wy][wx] == 0 : return False
  return True
  
def fill(x,y,width,value):
  for wy in range(y,y+width+1):
    for wx in range(x,x+width+1):
      paper_list[wy][wx] = value

def dfs(cnt, pnt, left_ones):
  global answer
  if pnt > 100 or cnt >= answer :
    return
  if left_ones == 0 :
    answer = min(cnt, answer)
    return

  for i in range(pnt, 100):
    x, y = i%10, i//10
    if paper_list[y][x] == 0 : continue
    for width in range(4,-1,-1):
      new_left_ones = left_ones-(width+1)**2
      if enabled_papers[width] == 0 or x+width>9 or y+width>9 : continue
      if check(x,y,width) and not visited[i][cnt+1][new_left_ones]:
        visited[i][cnt+1][new_left_ones] = True
        enabled_papers[width] -= 1
        fill(x,y,width,0)

        dfs(cnt+1,i+width+1,new_left_ones)
        fill(x,y,width,1)
        enabled_papers[width] += 1
  
dfs(0,0,left_ones)
print(answer if answer < 26 else -1)
