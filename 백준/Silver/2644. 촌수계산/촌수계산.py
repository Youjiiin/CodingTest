n = int(input())
a, b = map(int, input().split())
m = int(input())
family = [[] for _ in range(n + 1)]
for i in range(m):
    parent, child = map(int, input().split())
    family[parent].append(child)
    family[child].append(parent)
visited = [False] * (n + 1)
result = []

def dfs(v, count):
    visited[v] = True
    count += 1

    if v == b:
        result.append(count)

    for i in family[v]:
        if visited[i] == False:
            dfs(i, count)

dfs(a, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0] - 1)