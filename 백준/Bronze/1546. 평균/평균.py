n = int(input())
score = list(map(int, input().split()))
sum = 0
m = max(score)

for i in score:
    a = i / m * 100
    sum += a
print(sum / n)