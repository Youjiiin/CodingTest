from collections import deque

n, m = map(int, input().split())
num = deque(map(int, input().split()))
nums = deque(range(1, n + 1))

# 2번 방법
def second():
    nums.rotate(-1)

# 3번 방법
def third():
    nums.rotate(1)

count = 0

for target in num:
    while nums[0] != target:
        mid = len(nums) // 2

        if nums.index(target) <= mid:
            second()
        else:
            third()

        count += 1
    nums.popleft()

print(count)