from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y, size):
    q = deque()
    q.append((x, y))
    visited = [[0] * n for _ in range(n)]
    distance = [[0] * n for _ in range(n)]
    visited[x][y] = 1
    temp = []

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] <= size:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[x][y] + 1
                    if graph[nx][ny] < size and graph[nx][ny] != 0:
                        temp.append((nx, ny, distance[nx][ny]))

    return sorted(temp, key=lambda x: (x[2], x[0], x[1]))

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
count = 0
x, y, size = 0, 0, 2

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x = i
            y = j


result = 0
while True:
    shark = bfs(x, y, size)

    # 더 이상 먹을 물고기 없으면 종료
    if not shark:
        break

    nx, ny, dist = shark[0]  # 가장 우선순위가 높은 물고기 선택

    result += dist  # 이동 거리(즉, 시간) 추가
    graph[x][y] = 0  # 상어의 초기 위치를 빈 칸으로 만듦
    x, y = nx, ny  # 상어의 위치 갱신
    graph[nx][ny] = 0  # 먹은 물고기의 위치를 빈 칸으로 만듦

    count += 1
    if count == size:  # 상어 크기만큼 물고기를 먹었으면 크기 증가
        size += 1
        count = 0
print(result)