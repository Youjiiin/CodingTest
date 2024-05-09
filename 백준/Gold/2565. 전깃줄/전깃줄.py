from itertools import permutations
n = int(input())
elec = [list(map(int, input().split())) for _ in range(n)]
elec.sort()
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if elec[j][1] < elec[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))