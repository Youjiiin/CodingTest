n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(num[i])):
        if j == 0:
            num[i][j] += num[i - 1][j]
        elif j == (len(num[i]) - 1):
            num[i][j] += num[i - 1][j - 1]
        else:
            num[i][j] = max(num[i][j] + num[i - 1][j - 1], num[i][j] + num[i - 1][j])
print(max(num[-1]))