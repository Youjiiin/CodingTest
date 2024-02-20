s = input().split('-')
sum_list = []

for i in s:
    num = i.split("+")
    sum = 0
    for j in num:
        sum += int(j)
    sum_list.append(sum)

result = sum_list[0]
for i in range(1, len(sum_list)):
    result -= sum_list[i]
print(result)