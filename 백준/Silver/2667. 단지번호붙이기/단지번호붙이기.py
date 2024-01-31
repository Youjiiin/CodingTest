# DFS
import sys
input = sys.stdin.readline
n = int(input())
graph = []
count = 0
count_arr = []

#지도 입력받기
for _ in range(n):
    graph.append(list(map(int, input().strip())))

#dfs 함수
def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        global count
        count += 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False

#마을의 개수 세기
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            count_arr.append(count)
            count = 0

#출력
count_arr.sort()
print(len(count_arr))
for i in count_arr:
    print(i)