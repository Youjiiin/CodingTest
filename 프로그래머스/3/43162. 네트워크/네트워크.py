def dfs(v, visited, n, computers):
    visited[v] = True
    for i in range(n):
        if computers[v][i] == 1 and visited[i] == False:
            dfs(i, visited, n, computers)
            
def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(i, visited, n, computers)
            answer += 1
                
    return answer