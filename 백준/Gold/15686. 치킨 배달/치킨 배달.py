from itertools import combinations

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 99999
home = []
chicken = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append([i, j])
        elif graph[i][j] == 2:
            chicken.append([i, j])

for c in combinations(chicken, m):
    count = 0
    for h in home:
        length = 999
        for j in range(m):
            length = min(length, abs(h[0] - c[j][0]) + abs(h[1] - c[j][1]))
        count += length
    result = min(result, count)
print(result)