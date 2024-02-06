n = int(input())
r = []
for i in range(n):
    r.append(int(input()))
max_w = 0
r.sort()
for i in range(n):
    max_w = max(max_w, r[i] * (n - i))
print(max_w)