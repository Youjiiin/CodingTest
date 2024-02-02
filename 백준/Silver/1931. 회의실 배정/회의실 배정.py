import sys
input = sys.stdin.readline
n = int(input())

time = []
for i in range(n):
    time.append(tuple(map(int, input().split())))
time.sort(key = lambda x : (x[1], x[0]))

count = 0
end = 0
for a, b in time:
    if a >= end:
        count += 1
        end = b
print(count)