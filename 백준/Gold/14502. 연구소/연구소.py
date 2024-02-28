from collections import deque
from itertools import combinations
import copy
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

#감염 함수
def bfs(graph):
    q = deque()

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    q.append((nx, ny))
    
    global result
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1
    result = max(result, cnt)


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0
x_y = [(x, y) for y in range(m) for x in range(n) if not graph[x][y]]

for c in combinations(x_y, 3):
    graph_copy = copy.deepcopy(graph)
    for x, y in c:
        graph_copy[x][y] = 1
    bfs(graph_copy)

print(result)