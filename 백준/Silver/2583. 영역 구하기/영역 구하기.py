from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(x, y, count):
    q = deque()
    q.append((x, y))
    graph[x][y] = 1
    count += 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    count += 1
                    graph[nx][ny] = 1
                    q.append((nx, ny))
    return count

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

count_arr = []
for i in range(m):
    for j in range(n):
        count = 0
        if graph[i][j] == 0:
            count = bfs(i, j, count)
            count_arr.append(count)
count_arr.sort()
print(len(count_arr))
for i in count_arr:
    print(i, end=" ")