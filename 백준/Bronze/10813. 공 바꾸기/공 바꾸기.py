n, m = map(int, input().split())
basket = [0] * n

for a in range(n):
    basket[a] = a + 1

for _ in range(m):
    i, j = map(int, input().split())
    c = basket[i - 1]
    d = basket[j - 1]
    basket[j - 1] = c
    basket[i - 1] = d

for e in basket:
    print(e, end=" ")