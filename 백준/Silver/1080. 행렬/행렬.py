n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
result_arr = [list(map(int, input().strip())) for _ in range(n)]

def change(i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            if arr[x][y] == 0:
                arr[x][y] = 1
            else:
                arr[x][y] = 0

cnt = 0
if (n < 3 or m < 3) and arr != result_arr:
    cnt = -1
else:
    for i in range(n - 2):
        for j in range(m - 2):
            if arr[i][j] != result_arr[i][j]:
                cnt += 1
                change(i, j)

if cnt != -1:
    if arr != result_arr:
        cnt = -1
print(cnt)