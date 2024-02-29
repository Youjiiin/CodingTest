from collections import deque

def bfs(v, target):
    visited = [False] * (n + 1)
    q = deque()
    q.append((v, 0))
    visited[v] = True

    while q:
        v, count = q.popleft()

        if v == target:
            return count
        
        for i in graph[v]:
            if visited[i] == False:
                visited[i] = True
                q.append((i, count + 1))
    return False

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

min_bacon = 5001
person = 101
for i in range(1, n + 1):
    bacon = 0
    for j in range(1, n + 1):
        if i != j:
            dis = bfs(i, j)
            if dis:
                bacon += dis
    if min_bacon > bacon:
        min_bacon = bacon
        person = i

print(person)