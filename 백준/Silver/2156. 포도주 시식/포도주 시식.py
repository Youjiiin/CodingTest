n = int(input())
grape = [0] * (n + 1)
for i in range(1, n + 1):
    grape[i] = int(input())

drink = [0] * (n + 1)
drink[1] = grape[1]
if n > 1:
    drink[2] = grape[1] + grape[2]

for i in range(3, n + 1):
    drink[i] = max(drink[i - 3] + grape[i - 1] + grape[i], drink[i - 2] + grape[i], drink[i - 1])

print(drink[n])