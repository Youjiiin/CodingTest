from collections import deque

n, k = map(int, input().split())
visited = [-1] * 100001
visited[n] = 0

def bfs(a):
    q = deque([a])

    while q:
        x = q.popleft()

        if x == k:
            print(visited[k])
            return

        if 0 <= 2 * x <= 100000 and visited[2 * x] == -1:
            visited[2 * x] = visited[x]
            q.append(2 * x)

        for nx in (x - 1, x + 1):
            if 0 <= nx <= 100000 and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                q.append(nx)

bfs(n)