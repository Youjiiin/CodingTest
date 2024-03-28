import sys
input = sys.stdin.readline

# 사다리의 결과를 확인하는 함수
def checkResult():
    for i in range(n):
        now = i
        for j in range(h):
            # 가로선이 오른쪽으로 이어져 있다면,
            if line[j][now]:
                now += 1
            # 가로선 왼쪽, now > 0을 안해줬었음
            elif now > 0 and line[j][now - 1]:
                now -= 1

        # i번째 시작, 결과 i
        if now != i:
            return False
    return True

def dfs(x, y, count):
    global answer

    if answer <= count:
        return
    if checkResult():
        answer = min(answer, count)
        return
    if count == 3:  # 최대 가로선 개수는 3으로 제한
        return

    for i in range(x, h):
        # y가 0이 아니라면 현재 행에서 시작, 그렇지 않으면 다음 행부터
        k = y if i == x else 0
        for j in range(k, n - 1):
            if not line[i][j] and (j == 0 or not line[i][j-1]) and not line[i][j+1]:
                line[i][j] = True
                # 가로선을 추가한 다음 위치부터 다시 탐색 시작
                dfs(i, j + 2, count + 1)
                line[i][j] = False


# 세로선 개수, 가로선 개수, 세로선마다 가로선을 놓을 수 있는 위치의 개수
n, m, h = map(int, input().split())
# 이미 그어진 선의 위치(a번 점선, b와 b + 1이 연결)
line = [[0] * n for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    line[a - 1][b - 1] = 1
answer = 4

dfs(0, 0, 0)
if answer > 3:
    answer = -1
print(answer)