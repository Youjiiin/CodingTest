from collections import deque

# 방향 벡터 정의
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 최단 거리 찾기
def bfs(start_x, start_y, n, board):
    q = deque()
    q.append((start_x, start_y))
    visited = [[-1] * n for _ in range(n)]
    visited[start_x][start_y] = 0

    while q:       
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    return visited

# 가장 가까운 승객 구하기
def check_near(visited, people):
    min_distance = int(1e9)
    minx, miny = -1, -1
    min_idx = -1
    for idx, (sx, sy, ex, ey) in enumerate(people):
        if visited[sx][sy] != -1 and visited[sx][sy] < min_distance:
            min_distance = visited[sx][sy]
            minx, miny = sx, sy
            min_idx = idx
        elif visited[sx][sy] == min_distance:
            if (sx, sy) < (minx, miny):
                minx, miny = sx, sy
                min_idx = idx
    return minx, miny, min_distance, min_idx

n, m, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
nowx, nowy = map(int, input().split())
nowx -= 1
nowy -= 1

people = [list(map(int, input().split())) for _ in range(m)]
# 좌표 수정
for i in range(m):
    people[i][0] -= 1
    people[i][1] -= 1
    people[i][2] -= 1
    people[i][3] -= 1

for _ in range(m):
    if fuel <= 0:
        fuel = -1
        break

    vst = bfs(nowx, nowy, n, board)
    nowx, nowy, dist, min_idx = check_near(vst, people)
    if nowx == -1 and nowy == -1:
        fuel = -1
        break

    fuel -= dist
    if fuel < 0:
        fuel = -1
        break

    ex, ey = people[min_idx][2], people[min_idx][3]
    people.pop(min_idx)

    vst = bfs(nowx, nowy, n, board)
    dist = vst[ex][ey]
    if dist == -1 or fuel < dist:
        fuel = -1
        break

    fuel += dist
    nowx, nowy = ex, ey

print(fuel)
