n, m = map(int, input().split())
num = []

def dfs(start):
    if len(num) == m:
        print(" ".join(map(str, num)))
        return
    
    for i in range(start, n + 1):
        num.append(i)
        dfs(i)
        num.pop()

dfs(1)