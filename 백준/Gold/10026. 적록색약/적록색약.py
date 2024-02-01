import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = []
visited = [[False] * n for _ in range(n)]
dx = [1, -1, 0 ,0]
dy = [0, 0, 1, -1]
for _ in range(n):
    graph.append(list(map(str, input().strip())))

def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == False and graph[nx][ny] == graph[x][y]:
                dfs(nx, ny)

#아닌 사람
count1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            count1 += 1

#빨간색 -> 초록색
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] ='G'

visited = [[False] * n for _ in range(n)]

#적록색약인 사람
count2 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            count2 += 1

print(count1, count2)