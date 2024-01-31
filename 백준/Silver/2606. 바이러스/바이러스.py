from collections import deque
#BFS로 풀어야함
n = int(input()) # 노드의 수
m = int(input()) # 간선의 수
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0

#bfs 함수
def bfs(node, count):
    q = deque([node])
    visited[node] = True

    while q:
        v = q.popleft()
        count += 1

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    return count

#연결 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(1, count) - 1)