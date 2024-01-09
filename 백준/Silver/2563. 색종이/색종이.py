t = int(input())
s = [[0] * 100 for _ in range(100)]

for _ in range(t):
    y, x = map(int, input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            s[i][j] = 1

r = 0
for i in range(100):
    r += s[i].count(1)
print(r)