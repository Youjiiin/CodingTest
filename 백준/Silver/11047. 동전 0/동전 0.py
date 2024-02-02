n, k = map(int, input().split())
money = []
for _ in range(n):
    money.append(int(input()))
money.reverse()

count = 0
for i in money:
    count += k // i
    k = k % i

print(count)