from itertools import combinations
n, s = map(int, input().split())
num = list(map(int, input().split()))
count = 0

for i in range(1, n + 1):
    for c in combinations(num, i):
        if sum(c) == s:
            count += 1
print(count)