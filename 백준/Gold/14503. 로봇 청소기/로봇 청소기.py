from collections import deque

n, m = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 1

def bfs(x, y, d):
    global count
    q = deque()
    q.append((x, y))
    arr[x][y] = 2

    while q:
        x, y = q.popleft()
        flag = 0

        for _ in range(4):
            d = (d + 3) % 4
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                arr[nx][ny] = 2
                q.append((nx, ny))
                count += 1
                flag = 1
                break

        if flag == 0:
            if arr[x - dx[d]][y - dy[d]] != 1:
                q.append((x - dx[d], y - dy[d]))
            else:
                print(count)
                break
bfs(x, y, d)