from collections import deque

n, l, r = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 이웃나라의 인구 수 차이 확인 + 연합
def check_neighbor(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    union = []
    union.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] == 0:
                if l <= abs(world[x][y] - world[nx][ny]) <= r:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    union.append((nx, ny))

    # 연합이 없다면
    if len(union) <= 1:
        return 0
    
    # 인구 분배
    people = sum(world[x][y] for x, y in union) // len(union)
    for a, b in union:
        world[a][b] = people
    return 1

day = 0
while 1:
    tmp = 0
    visited = [[0] * n for _ in range(n)] 
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                tmp += check_neighbor(i, j)

    if tmp == 0:
        break
    day += 1
print(day)   