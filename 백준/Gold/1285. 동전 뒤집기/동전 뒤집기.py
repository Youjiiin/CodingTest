n = int(input())
board = []
for _ in range(n):
    row = input().strip()
    board.append(list(row))
min_T = int(1e9)

# # 뒤집기(행)
# def flip_row(row):
#     for i in range(n):
#         if board[row][i] == 'T':
#             board[row][i] = 'H'
#         else:
#             board[row][i] = 'T'

# # 뒤집기(열)
# def flip_column(col):
#     for i in range(n):
#         if board[i][col] == 'T':
#             board[i][col] = 'H'
#         else:
#             board[i][col] = 'T'

# # 뒷면 개수 세기
# def count_H():
#     count = 0
#     for i in range(n):
#         for j in range(n):
#             if board[i][j] == 'T':
#                 count += 1
#     return count

# # 일단 뒤집기
# for i in range(n):
#     flip_row(i)
#     min_T = min(count_H(), min_T)
#     for j in range(n):
#         flip_column(j)
#         min_T = min(count_H(), min_T)
# print(min_T)

for bit in range(1 << n):
    # 임시 보드를 원본 보드의 복사본으로 초기화
    tmp = [board[i][:] for i in range(n)]
    
    # 각 비트에 대해 행을 뒤집기
    for i in range(n):
        if bit & (1 << i):
            for j in range(n):
                if tmp[i][j] == 'H':
                    tmp[i][j] = 'T'
                else:
                    tmp[i][j] = 'H'
    
    # 각 열에서 'T'의 최소 개수를 계산
    tsum = 0
    for j in range(n):
        cnt_T = 0
        for i in range(n):
            if tmp[i][j] == 'T':
                cnt_T += 1
        # 'T'의 개수와 'H'의 개수 중 최소값을 더함
        tsum += min(cnt_T, n - cnt_T)
    
    # 최소값 갱신
    min_T = min(min_T, tsum)

print(min_T)