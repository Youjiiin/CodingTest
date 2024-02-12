n = int(input())
s = [0] * 1001

s[1] = 1
s[2] = 3
for i in range(3, n + 1):
    if i % 2 == 0:
        s[i] = (4 * s[i - 2]) - 1
    else:
        s[i] = (4 * s[i - 2]) + 1
print(s[n]%10007)