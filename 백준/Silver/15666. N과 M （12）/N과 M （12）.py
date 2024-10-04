n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

answer = []

def backtracking(depth):
    if len(answer) == m:
        print(*answer)
        return
    
    use = 0
    for i in range(depth, n):
        if use != nums[i]:
            answer.append(nums[i])
            use = nums[i]
            backtracking(i)
            answer.pop()

backtracking(0)