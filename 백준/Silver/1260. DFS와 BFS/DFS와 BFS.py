import sys
from collections import deque

input = sys.stdin.readline

n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited1 = [False] * (n + 1)
visited2 = [False] * (n + 1)

# 그래프 인접 리스트 생성
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 인접 리스트 정렬
for i in range(1, n + 1):
    graph[i].sort()

# DFS
def dfs(v):
    visited1[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited1[i]:
            dfs(i)

# BFS
def bfs(start):
    queue = deque([start])
    visited2[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited2[i]:
                queue.append(i)
                visited2[i] = True

dfs(start)
print()
bfs(start)
