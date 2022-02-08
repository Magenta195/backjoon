n = map(int, input().split())
s = 0
for i in n:
    s += i ** 2
print(s % 10)
