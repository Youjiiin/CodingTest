n = int(input())
count = [0] * (n + 1)
path = ["" for _ in range(n + 1)]
path[1] = "1"

for i in range(2, n + 1):
    count[i] = count[i - 1] + 1
    prev = i - 1

    if i % 2 == 0 and count[i//2] + 1 < count[i]:
        count[i] = count[i//2] + 1
        prev = i // 2

    if i % 3 == 0 and count[i//3] + 1 < count[i]:
        count[i] = count[i//3] + 1
        prev = i // 3

    path[i] = str(i) + " " + path[prev]

print(count[n])
print(path[n])
