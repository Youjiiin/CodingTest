n, k = map(int, input().split())

result = [list(map(int, input().split())) for _ in range(n)]
result.sort(key = lambda x: (x[1], x[2], x[3]), reverse=True)

idx = [result[i][0] for i in range(n)].index(k)
print(idx)
