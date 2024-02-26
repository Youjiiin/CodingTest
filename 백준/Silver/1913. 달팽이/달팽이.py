n = int(input())
target = int(input())
arr = [[0] * n for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = n//2, n//2

num = 1
arr[x][y] = num
rx, ry = 0, 0
num += 1

if target == 1:
    rx, ry = (n//2) + 1, (n//2) + 1

for i in range(1, n//2 + 1):
    if num == 2:
        nx, ny = x - 1, y - 1
    else:
        nx, ny = nx - 1, ny - 1

    step = i * 2
    for j in range(4):
        for k in range(step):
            nx = nx + dx[j]
            ny = ny + dy[j]
            arr[nx][ny] = num
            if num == target:
                rx, ry = nx + 1, ny + 1
            num += 1
for i in arr:
    for j in i:
        print(j, end=" ")
    print()

print(rx, ry)