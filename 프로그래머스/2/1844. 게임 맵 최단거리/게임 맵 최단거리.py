from collections import deque
def bfs(x, y, maps):
    n = len(maps)
    m = len(maps[0])
    q = deque()
    q.append((x, y))
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 0:
                continue
                
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
    return maps[n-1][m-1]

def solution(maps):
    answer = bfs(0, 0, maps)
    if answer == 1:
        return -1
    else:
        return answer