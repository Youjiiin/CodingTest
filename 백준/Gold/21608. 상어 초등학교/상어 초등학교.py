n = int(input())
likes = [list(map(int, input().split())) for _ in range(n**2)]
seat = [[0] * n for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 학생 선호 목록 딕셔너리로 구성
student_preferences = {like[0]: like[1:] for like in likes}

# 모든 학생 배치
for student, preferences in student_preferences.items():
    positions = []
    for i in range(n):
        for j in range(n):
            if seat[i][j] == 0:
                like = 0
                blank = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if seat[nx][ny] in preferences:
                            like += 1
                        if seat[nx][ny] == 0:
                            blank += 1
                positions.append([like, blank, i, j])
    positions.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    seat[positions[0][2]][positions[0][3]] = student

# 점수 계산
result = 0
for i in range(n):
    for j in range(n):
        s = 0
        current_student = seat[i][j]
        preferences = student_preferences[current_student]
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if seat[nx][ny] in preferences:
                    s += 1
        if s > 0:
            result += 10 ** (s - 1)

print(result)
