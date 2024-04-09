from collections import deque

def bfs():
    # 치즈가 녹고 난 이후에 계속 사용해야하기에 함수안에 위치
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1

    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                # 탐색하는 공기의 상하좌우에 치즈가 있으면,(공기에 노출된 면이 있음)
                if graph[nx][ny] >= 1:
                    graph[nx][ny] += 1
                else:
                    q.append((nx, ny))
                    visited[nx][ny] = 1

# 치즈 녹이기 함수
def melt():
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3:
                graph[i][j] = 0
                count += 1
            elif graph[i][j] >= 2:
                graph[i][j] = 1
    return count

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
time = 0

while True:
    bfs() # 녹을 치즈가 있는지 확인
    cheeze = melt() # 치즈 녹이기

    if cheeze:
        time += 1
    else:
        print(time)
        break