n, m = map(int, input().split())
basket = [a for a in range(1, n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    t = basket[i - 1:j]
    t.reverse()
    basket[i - 1:j] = t

for d in basket:
    print(d, end=" ")