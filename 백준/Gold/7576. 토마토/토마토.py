from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
  
def bfs():
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
bfs()

none = False
day = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            none = True
        day = max(day, graph[i][j])

if none == True:
    print(-1)
else:
    print(day - 1)