n = int(input())
t = []
p = []
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

get_money = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    if t[i] + i <= n:
        get_money[i] = max(p[i] + get_money[i + t[i]], get_money[i + 1])
    else:
        get_money[i] = get_money[i + 1]
print(get_money[0])