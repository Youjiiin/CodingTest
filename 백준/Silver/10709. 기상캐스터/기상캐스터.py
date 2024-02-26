h, w = map(int, input().split())
arr = [list(map(str, input().strip())) for _ in range(h)]
answer = [[-1] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if arr[i][j] == 'c':
            answer[i][j] = 0

for i in range(h):
    for j in range(1, w):
        if answer[i][j - 1] != -1 and answer[i][j] != 0:
            answer[i][j] = answer[i][j - 1] + 1

for i in range(h):
    for j in range(w):
        print(answer[i][j], end=" ")
    print()