from collections import deque

def bfs():
    q = deque()
    q.append((homex, homey))
    while q:
        x, y = q.popleft()
        if abs(x - festivalx) + abs(y - festivaly) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                convx, convy = store[i]
                if abs(x - convx) + abs(y - convy) <= 1000:
                    visited[i] = True
                    q.append((convx, convy))
    print('sad')

case = int(input())
for _ in range(case):
    n = int(input())
    homex, homey = map(int, input().split())
    store = []
    for i in range(n):
        x, y = map(int, input().split())
        store.append((x, y))
    festivalx, festivaly = map(int, input().split())
    visited = [False] * (n + 1)
    bfs()