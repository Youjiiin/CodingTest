n = int(input())
num = [i for i in range(n + 1)]

for i in range(2, n + 1):
    for j in range(1, i + 1):
        if j * j > i:
            break
        if num[i] > num[i - j*j] + 1:
            num[i] = num[i - j*j] + 1
print(num[n])