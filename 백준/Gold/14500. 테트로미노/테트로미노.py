dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def dfs(x, y, idx, total):
    global max_sum
    if max_sum >= total + max_val * (3 - idx):
        return
    if idx == 3:
        max_sum = max(max_sum, total)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if idx == 1:
                    visited[nx][ny] = 1
                    dfs(x, y, idx + 1, total + num[nx][ny])
                    visited[nx][ny] = 0
                visited[nx][ny] = 1
                dfs(nx, ny, idx + 1, total + num[nx][ny])
                visited[nx][ny] = 0

n, m = map(int, input().split())
num = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
max_sum = 0
max_val = max(map(max, num))

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 0, num[i][j])
        visited[i][j] = 0

print(max_sum)