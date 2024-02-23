answer = 0
def dfs(numbers, target, num, idx):
    global answer

    if idx == len(numbers):
        if num == target:
            answer += 1
        return
    
    else:
        dfs(numbers, target, num + numbers[idx], idx + 1)
        dfs(numbers, target, num - numbers[idx], idx + 1)
    
def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return answer