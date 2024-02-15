a, b, c = map(int, input().split())
i1, o1 = map(int, input().split())
i2, o2 = map(int, input().split())
i3, o3 = map(int, input().split())
time = [0] * 100
for i in range(i1, o1):
    time[i] += 1
for i in range(i2, o2):
    time[i] += 1
for i in range(i3, o3):
    time[i] += 1

total = 0
for i in time:
    if i == 1:
        total += (i * a)
    elif i == 2:
        total += (i * b)
    elif i == 3:
        total += (i * c)
print(total)