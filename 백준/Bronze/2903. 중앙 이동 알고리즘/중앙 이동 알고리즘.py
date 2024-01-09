n = int(input())
a = 2

for i in range(1, n + 1):
    a += 2**(i - 1)

print(a**2)