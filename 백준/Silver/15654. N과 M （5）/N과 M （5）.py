n, m = map(int, input().split())
num = list(map(int, input().split()))

num.sort()

def backtracking(depth):
    if depth == m:
        print(' '.join(map(str, box)))
        return
    
    for i in range(n):
        if num[i] in box:
            continue
        box.append(num[i])
        backtracking(depth + 1)
        box.pop()

box = []
backtracking(0)