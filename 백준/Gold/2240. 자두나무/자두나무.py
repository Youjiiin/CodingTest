t, w = map(int, input().split())
time = [0] + [int(input()) for _ in range(t)]
dp = [[0] * (w + 1) for _ in range(t + 1)]

for i in range(t + 1):
    # 1번 나무에서 떨어질 때
    if (time[i] == 1):
        dp[i][0] = dp[i - 1][0] + 1
    
    # 2번 나무에서 떨어질 때
    else:
        dp[i][0] = dp[i - 1][0]
    
    for j in range(1, w + 1):
        # 이동 횟수가 홀수면 2번 나무에 위치해 있다는 뜻
        if (time[i] == 2 and j % 2 == 1):
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1
        # 이동 횟수가 짝수면 1번 나무에 위치해 있다는 뜻
        elif (time[i] == 1 and j % 2 == 0):
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1
        # 나무의 위치가 다르다면
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j])
print(max(dp[t]))