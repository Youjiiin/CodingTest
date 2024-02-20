n = int(input())
plus = []
minus = []
sum = 0
for _ in range(n):
    i = int(input())
    if i <= 0:
        minus.append(i)
    elif i > 1:
        plus.append(i)
    else:
        sum += i

plus.sort(reverse=True)
minus.sort()


for i in range(0, len(plus), 2):
    if i + 1 < len(plus):
        sum += plus[i] * plus[i + 1]
    else:
        sum += plus[i]

for i in range(0, len(minus), 2):
    if i + 1 < len(minus):
        sum += minus[i] * minus[i + 1]
    else:
        sum += minus[i]

print(sum)