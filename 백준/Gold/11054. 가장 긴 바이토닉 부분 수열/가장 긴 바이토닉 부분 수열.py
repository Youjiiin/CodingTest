n = int(input())
num = list(map(int, input().split()))
num_rever = num[::-1]
dp = [1] * n
dp2 = [1] * n

for i in range(1, n):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j] + 1)
        if num_rever[i] > num_rever[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)
dp2.reverse()
max_n = 0
for i in range(n):
    max_n = max(max_n, dp[i] + dp2[i] - 1)
print(max_n)