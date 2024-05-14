h, w = map(int, input().split())
blocks = list(map(int, input().split()))
sum = 0

for i in range(1, w - 1):
    left_max = max(blocks[:i])
    right_max = max(blocks[i+1:])

    compare = min(left_max, right_max)

    if blocks[i] < compare:
        sum += compare - blocks[i]

print(sum)