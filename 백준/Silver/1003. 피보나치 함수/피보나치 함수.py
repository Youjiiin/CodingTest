t = int(input())
for i in range(t):
    n = int(input())
    if n == 0:
        print('1 0')
    elif n == 1:
        print('0 1')
    else:
        dp = [[0, 0] for _ in range(n + 1)]
        dp[0][0] = 1
        dp[0][1] = 0
        dp[1][0] = 0
        dp[1][1] = 1

        for j in range(2, n + 1):
            dp[j][0] = dp[j - 1][0] + dp[j - 2][0]
            dp[j][1] = dp[j - 1][1] + dp[j - 2][1]

        print(*dp[n])