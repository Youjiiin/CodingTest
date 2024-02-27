n, k = map(int, input().split())
table = list(map(str, input().strip()))
visited = [False] * n
cnt = 0
for i in range(n):
    if table[i] == 'P':
        for j in range(max(0, i - k), min(n, i + k + 1)):
            if table[j] == 'H' and not visited[j]:
                visited[j] = True
                cnt += 1
                break
print(cnt)