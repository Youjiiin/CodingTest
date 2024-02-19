n = int(input())
pn = [0] * (n + 1)
if n == 1 or n == 2:
    print(1)
else:
    pn[1] = 1
    pn[2] = 1
    for i in range(3, n+1):
        pn[i] = pn[i-1] + pn[i-2]
    print(pn[-1])