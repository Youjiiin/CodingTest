dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, color, count):
    graph[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if graph[nx][ny] == color:
                count = dfs(nx, ny, color, count + 1)
    return count
        
n, m = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(m)]

white = 0
black = 0

for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W':
            white += (dfs(i, j, 'W', 1)) ** 2
        elif graph[i][j] == 'B':
            black += (dfs(i, j, 'B', 1)) ** 2
print(white, black)