a = []
count = 0

for i in range(10):
    n = int(input())
    a.append(n % 42)

a = set(a)
a = list(a)

for i in a:
    count += 1
print(count)