import sys
input = sys.stdin.readline

n, m = map(int, input().split())
poketmon = {}

for i in range(1, n + 1):
    name = input().strip()
    poketmon[i] = name
    poketmon[name] = i

for i in range(m):
    q = input().strip()

    if q.isdigit():
        print(poketmon[int(q)])
    else:
        print(poketmon[q])