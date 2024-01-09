t = int(input())
q = 0
d = 0
n = 0

for _ in range(t):
    money = int(input())
    q = money // 25
    money %= 25
    d = money // 10
    money %= 10
    n = money // 5
    money %= 5
    print(q, d, n, money)