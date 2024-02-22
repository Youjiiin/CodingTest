t = int(input())
for _ in range(t):
    q = list(map(str, input().strip()))
    sum = 0
    count = 0
    for i in q:
        if i == 'O':
            count += 1
        else:
            count = 0
        sum += count
    
    print(sum)