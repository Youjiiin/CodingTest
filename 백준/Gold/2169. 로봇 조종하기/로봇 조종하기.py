n, m = map(int, input().split())
value = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dp[0][0] = value[0][0]

for j in range(1, m):
    # 오른쪽으로 밖에 못가므로 첫째줄은 그냥 누적합
    dp[0][j] = value[0][j] + dp[0][j - 1]

# 오른쪽 방향, 왼쪽 방향 나눠서 계산 후, 큰 값을 채택
for i in range(1, n):
    to_right = [0] * m
    to_left = [0] * m

    to_right[0] = value[i][0] + dp[i - 1][0]
    to_left[m - 1] = value[i][m - 1] + dp[i - 1][m - 1]

    # 왼쪽 방향으로 가는 경우
    for j in range(1, m):
        to_right[j] = value[i][j] + max(dp[i - 1][j], to_right[j - 1])
    # 오른쪽 방향으로 가는 경우
    for j in range(m - 2, -1, -1):
        to_left[j] = value[i][j] + max(dp[i - 1][j], to_left[j + 1])

    max_dp = [max(to_right[k], to_left[k]) for k in range(m)]

    for j in range(m):
        dp[i][j] = max_dp[j]

print(dp[n-1][m-1])