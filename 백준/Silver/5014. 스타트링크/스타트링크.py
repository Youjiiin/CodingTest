from collections import deque

f, s, g, u, d = map(int, input().split())
visited = [0] * (f + 1)

def bfs():
    q = deque([s])
    visited[s] = 1

    while q:
        x = q.popleft()
        
        if x == g:
            return visited[g] - 1

        for i in [u, -d]:
            if 0 < x + i <= f and not visited[x + i]:
                visited[x + i] = visited[x] + 1
                q.append(x + i)

    return "use the stairs"

print(bfs())