n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [0] * n
answer = []

def backtracking(depth):
    if len(answer) == m:
        print(*answer)
        return
    
    use = 0
    for i in range(depth, n):
        if use != nums[i] and not visited[i]:
            visited[i] = 1
            answer.append(nums[i])
            use = nums[i]
            backtracking(i + 1)
            visited[i] = False
            answer.pop()
            
backtracking(0)