n = list(input().strip())
n.sort(reverse=True)
if '0' in n:
    sum = 0
    for i in n:
        sum += int(i)
    if sum % 3 == 0:
        print("".join(n))
    else:
        print(-1)
else:
    print(-1)