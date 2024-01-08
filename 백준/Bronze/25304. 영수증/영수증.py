budget = int(input())
num = int(input())
sum = 0

for i in range(1, num + 1):
    m, n = map(int, input().split(" "))
    sum += (m * n)
    
if sum == budget:
    print("Yes")
else:
    print("No")