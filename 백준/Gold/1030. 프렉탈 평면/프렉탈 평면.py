import sys
input = sys.stdin.readline

def paint(x, y, size):
    newSize = size // n

    # 중앙 검은색 영역을 확인
    blackStart = (n - k) // 2 * newSize
    blackEnd = ((n + k) // 2) * newSize

    # size 1일 때(흰색 하나만 있어야 함)
    if size <= 1:
        return 0
    
    # 정중앙(검정색이어야 함)
    if blackStart <= x < blackEnd and blackStart <= y < blackEnd:
        return 1
    else:
        x %= newSize
        y %= newSize

        return paint(x, y, newSize)
    

# 시간, n*n, k*k
s, n, k, r1, r2, c1, c2 = map(int, input().split())
side = n ** s

for i in range(r1, r2 + 1):
    for j in range(c1, c2 + 1):
        print(paint(i, j, side), end="")
    print()