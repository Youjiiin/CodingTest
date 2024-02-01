import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = []
max_height = 0
for _ in range(n):
    arr = list(map(int, input().split()))
    max_height = max(max_height, max(arr))
    graph.append(arr)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, w, visited):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == False and graph[nx][ny] > w:
                dfs(nx, ny, w, visited)

max_count = 0
for w in range(max_height):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
                if visited[i][j] == False and graph[i][j] > w:
                    dfs(i, j, w, visited)
                    visited[i][j] = True
                    count += 1
    max_count = max(max_count, count)
print(max_count)