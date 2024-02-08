n = int(input())
tn = [a * (a + 1) // 2 for a in range(1, 46)]
num_arr = [0] * 1001

for i in tn:
    for j in tn:
        for k in tn:
            num = i + j + k
            if num <= 1000:
                num_arr[num] = 1

for i in range(n):
    inp = int(input())
    print(num_arr[inp])