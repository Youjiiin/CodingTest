import sys
input = sys.stdin.readline

# 빙고판
board = [list(map(int, input().split())) for _ in range(5)]

# 사회자가 말한 순서
l = []
for _ in range(5):
    l += map(int, input().split())

def bingo_check():
    bingo = 0

    # 가로 확인
    for a in board:
        if a.count(0) == 5:
            bingo += 1

    # 세로 확인
    for a in range(5):
        row = 0
        for b in range(5):
            if board[b][a] == 0:
                row += 1

        if row == 5:
            bingo += 1

    # 대각선 1
    d1 = 0
    for i in range(5):
        if board[i][i] == 0:
            d1 += 1
    if d1 == 5:
        bingo += 1
    
    # 대각선 2
    d2 = 0
    for i in range(5):
        if board[i][4 - i] == 0:
            d2 += 1
    if d2 == 5:
        bingo += 1

    return bingo

check = 0
for i in range(25):
    for a in range(5):
        for b in range(5):
            if l[i] == board[a][b]:
                board[a][b] = 0
                check += 1

    if check >= 12:
        score = bingo_check()

        if score >= 3:
            print(i + 1)
            break
            