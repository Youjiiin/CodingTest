n = int(input())
candy = [list(map(str, input().strip())) for _ in range(n)]

def check(candy):
    max_count = 1
    for i in range(n):
        count = 1
        for j in range(1, n):
            if candy[i][j] == candy[i][j - 1]:
                count += 1
            else:
                count = 1
            max_count = max(count, max_count)
        count = 1
        for j in range(1, n):
            if candy[j][i] == candy[j - 1][i]:
                count += 1
            else:
                count = 1
            max_count = max(count, max_count)
    return max_count

ans = 0
for i in range(n):
    for j in range(n):
        if j + 1 < n:
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
            ans = max(check(candy),ans)
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
        if i + 1 < n:
            candy[i][j], candy[i + 1][j] = candy[i + 1][j],candy[i][j]
            ans = max(check(candy),ans)
            candy[i][j], candy[i + 1][j] = candy[i + 1][j],candy[i][j]
print(ans)