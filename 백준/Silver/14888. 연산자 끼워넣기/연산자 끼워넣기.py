n = int(input())
num = list(map(int, input().split()))
cal = list(map(int, input().split())) # + - x /

max_cal = -1e9
min_cal = 1e9

def dfs(depth, total, plus, minus, multi, divine):
    global max_cal, min_cal
    if depth == n:
        max_cal = max(total, max_cal)
        min_cal = min(total, min_cal)
        return
    
    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multi, divine)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multi, divine)
    if multi:
        dfs(depth + 1, total * num[depth], plus, minus, multi - 1, divine)
    if divine:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multi, divine - 1)

dfs(1, num[0], cal[0], cal[1], cal[2], cal[3])
print(max_cal)
print(min_cal)