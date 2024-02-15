def b_sort(stu):
    count = 0
    for i in range(len(stu) - 1, 0, -1):
        for j in range(i):
            if stu[j] > stu[j + 1]:
                stu[j], stu[j + 1] = stu[j + 1], stu[j]
                count += 1
    return count

test = int(input())
for _ in range(test):
    a = list(map(int, input().split()))
    case, stu = a[0], a[1:]
    print(case, b_sort(stu))