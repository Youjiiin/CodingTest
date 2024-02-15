n = int(input())
switch = [-1] + list(map(int, input().split()))

def change(n):
    if switch[n] == 0:
        switch[n] = 1
    else:
        switch[n] = 0
    return

stu = int(input())
for _ in range(stu):
    gender, num = map(int, input().split())

    #남자일 때
    if gender == 1:
        for i in range(1, n + 1):
            if i % num == 0:
                change(i)
    
    else:
        if switch[num] == 0:
            switch[num] = 1
        else:
            switch[num] = 0
        for i in range(n//2):
            if num + i > n or num - i < 1:
                break
            if switch[num - i] == switch[num + i]:
                change(num - i)
                change(num + i)
            else:
                break

for i in range(1, n + 1):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()