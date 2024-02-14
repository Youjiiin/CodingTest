from collections import deque

m, n, h = map(int, input().split())
box = []
for i in range(h):
    box1 = []
    for j in range(n):
        box1.append(list(map(int, input().split())))
    box.append(box1)

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                q.append([i, j, k])

while q:
    z, x, y = q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
            if box[nz][nx][ny] == 0:
                box[nz][nx][ny] = box[z][x][y] + 1
                q.append((nz, nx, ny))

result = False
day = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                result = True
            day = max(day, box[i][j][k])
            
if result == True:
    print(-1)
else:
    print(day - 1)