n = int(input())
num_list = list(map(int, input().split(" ")))
num = int(input())
count = 0

for i in num_list:
    if i == num:
        count += 1
print(count)