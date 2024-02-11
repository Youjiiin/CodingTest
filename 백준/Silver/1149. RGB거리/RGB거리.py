n = int(input())
color = [0] * n

for i in range(n):
    color[i] = list(map(int, input().split()))

for i in range(1, n):
    color[i][0] = min(color[i - 1][1], color[i - 1][2]) + color[i][0]
    color[i][1] = min(color[i - 1][0], color[i - 1][2]) + color[i][1]
    color[i][2] = min(color[i - 1][0], color[i - 1][1]) + color[i][2]

print(min(color[n - 1]))