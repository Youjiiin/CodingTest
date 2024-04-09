from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    q = deque()
    q.append((x, y))

    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    
    count = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 'L' and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    count = max(count, visited[nx][ny])
                    q.append((nx, ny))

    return count - 1


n, m = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            ans = max(ans, bfs(i, j))
    
print(ans)