n = int(input())

if n == 1:
    print(1 % 15746)
else:
    a, b = 1, 2
    for i in range(2, n):
        a, b = b, (a + b)% 15746
    print(b)