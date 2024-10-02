n, m = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
visited = [False] * n

def backtracking():
    check = 0
    if len(box) == m:
        print(*box)
    
    for i in range(n):
        if check != numbers[i] and not visited[i]:
            box.append(numbers[i])
            visited[i] = True
            check = numbers[i]
            backtracking()
            box.pop()
            visited[i] = 0

box = []
backtracking()