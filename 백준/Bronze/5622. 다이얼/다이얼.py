call = input()
num = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

call = list(call)
n = []
sum = 0

for i in call:
    for j in num:
        if i in j:
            n.append(num.index(j) + 2)

for i in n:
    sum += (i + 1)
print(sum)