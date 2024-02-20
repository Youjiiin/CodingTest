import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    p = [list(map(int, input().split())) for _ in range(n)]
    p = sorted(p)
    count = 1
    top = p[0][1]

    for i in range(1, n):
        if top > p[i][1]:
            count += 1
            top = p[i][1]
    print(count)