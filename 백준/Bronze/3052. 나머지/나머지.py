a = []

for i in range(10):
    n = int(input())
    a.append(n % 42)

print(len(set(a)))