from collections import deque

gear = [deque(map(int, input().strip())) for _ in range(4)] 
k = int(input())
spin_list = [list(map(int, input().split())) for _ in range(k)]

def determine_spins(num, direction):
    # 이 함수는 각 회전 명령에 대해 회전할 톱니바퀴와 방향을 저장합니다.
    spins = [(num, direction)]
    # 왼쪽 톱니바퀴 확인
    d = direction
    for i in range(num, 0, -1):
        if gear[i][6] != gear[i - 1][2]:
            d *= -1
            spins.append((i - 1, d))
        else:
            break
    # 오른쪽 톱니바퀴 확인
    d = direction
    for i in range(num, 3):
        if gear[i][2] != gear[i + 1][6]:
            d *= -1
            spins.append((i + 1, d))
        else:
            break
    return spins

for num, direction in spin_list:
    num -= 1  # 인덱스 조정
    spins = determine_spins(num, direction)
    for n, d in spins:
        gear[n].rotate(d)

# 점수 계산
sum_score = sum((gear[i][0] == 1) << i for i in range(4))
print(sum_score)
