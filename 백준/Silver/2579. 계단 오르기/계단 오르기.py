n = int(input())
stairs = [0] + [int(input()) for _ in range(n)]

if n == 1:
    print(stairs[1])
elif n == 2:
    print(stairs[1] + stairs[2])
else:
    score = [0] * (n + 1)
    score[1] = stairs[1]
    score[2] = stairs[1] + stairs[2]
    score[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

    for i in range(4, n + 1):
        score[i] = max(stairs[i] + stairs[i - 1] + score[i - 3], stairs[i] + score[i - 2])

    print(score[n])