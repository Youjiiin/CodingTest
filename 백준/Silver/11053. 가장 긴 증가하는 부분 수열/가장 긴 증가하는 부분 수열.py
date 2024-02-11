n = int(input())
a = list(map(int, input().split()))
arr = [1] * 1001

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            arr[i] = max(arr[i], arr[j] + 1)
print(max(arr))