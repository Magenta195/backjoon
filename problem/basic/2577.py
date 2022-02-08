i = 1
for _ in range(3):
    i *= int(input())
for j in range(10):
    print(str(i).count(str(j)))
