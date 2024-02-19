n, k = map(int, input().split())
bag = [[0, 0]]
for _ in range(n):
    bag.append(list(map(int, input().split())))
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = bag[i][0]
        v = bag[i][1]

        if w <= j:
            dp[i][j] = max(dp[i - 1][j], v + dp[i - 1][j - w])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[n][k])