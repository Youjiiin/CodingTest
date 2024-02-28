import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + num[i - 1][j - 1]
for _ in range(m):
    start_x, start_y, end_x, end_y = map(int, input().split())

    result = dp[end_x][end_y] - dp[end_x][start_y - 1] - dp[start_x - 1][end_y] + dp[start_x - 1][start_y - 1]
    print(result)