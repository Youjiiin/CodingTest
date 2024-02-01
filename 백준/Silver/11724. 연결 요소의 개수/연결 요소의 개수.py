#DFS
import sys
#노드의 개수, 간선의 개수
sys.setrecursionlimit(10**6) # 재귀 깊이 설정
input=sys.stdin.readline
def dfs(v, graph, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i, graph, visited)
            
n, m = map(int, input().split())
visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i, graph, visited)
        count += 1
print(count)