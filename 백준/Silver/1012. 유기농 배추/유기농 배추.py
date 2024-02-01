#DFS
import sys
sys.setrecursionlimit(10000) # 재귀 깊이 설정
input = sys.stdin.readline
#t번의 테스트 케이스
t = int(input())
#가로길이, 세로길이, 배추 위치 개수(노드의 개수)

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False


for _ in range(t):  
    m, n, k = map(int, input().split())
    #배추의 위치
    graph = [[0] * m for _ in range(n)]
    count = 0

    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                count += 1
    print(count)