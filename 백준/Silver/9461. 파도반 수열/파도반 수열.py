t = int(input())
for _ in range(t):
    n = int(input())
    num = [0] + [1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 90
    if n < 7:
        print(num[n])
    else:
        for i in range(10, n + 1):
            num[i] = num[i - 5] + num[i - 1]
        print(num[n])