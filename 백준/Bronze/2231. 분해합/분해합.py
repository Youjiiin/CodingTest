n = int(input())

for i in range(1, n + 1):
    # 분해합
    num = sum(map(int, str(i)))
    isn = num + i
    if n == isn:
        print(i)
        break
    if n == i:
        print(0)
        break