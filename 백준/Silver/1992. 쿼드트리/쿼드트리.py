# 모두 같은 숫자인지 확인
def check_same(x, y, n):
    num = board[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if num != board[i][j]:
                num = -1
                break

    if num == -1:
        print('(', end='')
        n = n // 2
        check_same(x, y, n)
        check_same(x, y + n, n)
        check_same(x + n, y, n)
        check_same(x + n, y + n, n)
        print(')', end='')
    
    elif num == 0:
        print(0, end='')
    else:
        print(1, end='')

n = int(input())
board = [list(map(int, input().strip())) for _ in range(n)]
check_same(0, 0, n)