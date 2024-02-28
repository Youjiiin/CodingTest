from collections import deque
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]
def bfs(start_x, start_y, end_x, end_y):
    q = deque()
    q.append((start_x, start_y, 0))
    visited[start_x][start_y] = True

    while q:
        x, y, count = q.popleft()
        if x == end_x and y == end_y:
            return count
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx, ny, count + 1))

t = int(input())
for _ in range(t):
    l = int(input())
    chess = [[0] * l for _ in range(l)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    visited = [[False] * l for _ in range(l)]
    
    print(bfs(start_x, start_y, end_x, end_y))