def paint(x, y, size, n, k):
    # size가 1보다 작거나 같을 때, 전체 영역이 검은색 또는 흰색
    if size <= 1:
        return 0  # 흰색으로 처리
    
    # 현재 영역의 한 변의 길이
    newSize = size // n
    
    # 중앙 검은색 영역을 확인
    blackStart = (n - k) // 2 * newSize
    blackEnd = ((n + k) // 2) * newSize
    
    # 현재 위치가 중앙 검은색 영역에 있는지 확인
    if blackStart <= x < blackEnd and blackStart <= y < blackEnd:
        return 1  # 검은색
    else:
        # 현재 위치를 새 영역에 맞게 조정
        newX = x % newSize
        newY = y % newSize
        return paint(newX, newY, newSize, n, k)

# 입력 처리
s, n, k, r1, r2, c1, c2 = map(int, input().split())
side = n ** s

for i in range(r1, r2 + 1):
    for j in range(c1, c2 + 1):
        print(paint(i, j, side, n, k), end="")
    print()
