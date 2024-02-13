from collections import deque
a, b = map(int, input().split())
visited = [0] * 100001

def bfs(a):
    q = deque([a])

    while q:
        a = q.popleft()
        if a == b:
            print(visited[b])
            break
        da = [a + 1, a - 1, 2 * a]
        for i in da:
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[a] + 1
                q.append(i)

bfs(a)