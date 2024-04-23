from collections import deque

n, m, t = map(int, input().split())
circle = [deque(map(int, input().split())) for _ in range(n)]
info = [[int(x) for x in input().split()] for _ in range(t)]
# x배수의 원판을 d방향(0: 시계 방향, 1: 반시계 방향)으로 k번

# 회전하기
for tt in range(t):
    x, d, k = info[tt]
    # k번 만큼 d방향으로 회전 시키기
    for i in range(n):
        if (i + 1) % x == 0:
            if d == 0:
                circle[i].rotate(k)
            else:
                circle[i].rotate(-k)
    
    remove_num = []
    # 같은 원 안에서
    for i in range(n):
        for j in range(m - 1):
            if circle[i][j] != 0 and circle[i][j + 1] != 0 and circle[i][j] == circle[i][j + 1]:
                remove_num.append((i, j))
                remove_num.append((i, j + 1))

        if circle[i][0] != 0 and circle[i][-1] != 0 and circle[i][0] == circle[i][-1]:
            remove_num.append((i, 0))
            remove_num.append((i, m - 1))

    # 인접한 원에 대해서
    for j in range(m):
        for i in range(n - 1):
            if circle[i][j] != 0 and circle[i + 1][j] != 0 and circle[i][j] == circle[i + 1][j]:
                remove_num.append((i, j))
                remove_num.append((i + 1, j))

    remove_num = list(set(remove_num))
    for i in range(len(remove_num)):
        x, y = remove_num[i]
        circle[x][y] = 0

    if not remove_num:  # 숫자 제거가 없을 경우 평균값 조정
            total, count = 0, 0
            for i in range(n):
                total += sum(circle[i])
                count += len([x for x in circle[i] if x != 0])
            if count > 0:
                average = total / count
                for i in range(n):
                    for j in range(m):
                        if circle[i][j] != 0:
                            if circle[i][j] > average:
                                circle[i][j] -= 1
                            elif circle[i][j] < average:
                                circle[i][j] += 1
    else:  # 숫자 제거
        for i, j in remove_num:
            circle[i][j] = 0

# 최종 점수 계산
ans = sum(sum(c) for c in circle)
print(ans)