cnt = 0
def dfs(numbers, target, num, idx):
    global cnt
    if idx == len(numbers):
        if num == target:
            cnt += 1
        return
    dfs(numbers, target, num + numbers[idx], idx + 1)
    dfs(numbers, target, num - numbers[idx], idx + 1)
    
    
def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return cnt