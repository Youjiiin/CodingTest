from collections import deque

def bfs(v, computers, visited, n):
    q = deque()
    q.append(v)
    visited[v] = True
    
    while q:
        v = q.popleft()
        
        for i in range(n):
            if computers[v][i] == 1 and visited[i] == False:
                visited[i] = True
                q.append(i)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
            bfs(i, computers, visited, n)
            answer += 1
                
    return answer