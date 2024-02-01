import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
#graph = [[], [4, 6], [4], [5, 6], [1, 2, 7], [3], [3], [4]]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    for i in graph[v]:
        if visited[i] == False:
            visited[i] = v
            dfs(i)

for i in range(2, n + 1):
    dfs(1)
    print(visited[i])