n = int(input())
p = list(map(int, input().split()))
p.sort()

sum = 0
for i in range(len(p)):
    p_sum = 0
    for j in p[0:i + 1]:
        p_sum += j
    sum += p_sum

print(sum)