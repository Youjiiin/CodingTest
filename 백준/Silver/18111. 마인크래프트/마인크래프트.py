import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
block = [list(map(int, input().split())) for _ in range(n)]

ans = int(1e9)
height = 0

for i in range(257):
    use = 0
    take = 0

    for x in range(n):
        for y in range(m):
            if block[x][y] > i:
                use += block[x][y] - i
            else:
                take += i - block[x][y]

    if use + b >= take:
        if (use * 2) + take <= ans:
            ans = (use * 2) + take
            height = i
print(ans, height)