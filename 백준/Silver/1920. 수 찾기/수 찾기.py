import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
num.sort()
m = int(input())
nm = list(map(int, input().split()))

def binary(i):
    first = 0
    end = n - 1

    while first <= end:
        mid = (first + end) // 2
        if num[mid] == i:
            return True
        if i < num[mid]:
            end = mid - 1
        elif i > num[mid]:
            first = mid + 1

for i in range(m):
    if binary(nm[i]):
        print(1)
    else:   
        print(0)