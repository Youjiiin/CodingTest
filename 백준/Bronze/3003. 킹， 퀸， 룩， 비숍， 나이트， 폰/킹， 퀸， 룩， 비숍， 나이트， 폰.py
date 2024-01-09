own = list(map(int, input().split()))
c = [1, 1, 2, 2, 2, 8]
answer = []

for i in range(6):
    c[i] = c[i] - own[i]
    print(c[i], end=" ")