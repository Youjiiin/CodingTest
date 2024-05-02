n, d = map(int, input().split())
load = [list(map(int, input().split())) for _ in range(n)]
dp = [i for i in range(d + 1)]

for i in range(d + 1):
    if i > 0:
        dp[i] = min(dp[i], dp[i - 1] + 1)
    for s, e, j in load:
        if i == s and e <= d and dp[i] + j < dp[e]:
            dp[e] = dp[i] + j
print(dp[-1])