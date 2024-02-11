n = int(input())
stairs = [0] * 301
for i in range(1, n + 1):
    stairs[i] = int(input())

steps = [0] * 301
steps[1] = stairs[1]
steps[2] = stairs[1] + stairs[2]
steps[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, n + 1):
    steps[i] = max(steps[i - 3] + stairs[i - 1] + stairs[i], steps[i - 2] + stairs[i])
print(steps[n])