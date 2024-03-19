# 부등호가 성립하는 지 확인하는 함수
def check(x, y, s):
    if s == '>':
        if x < y:
            return False
    else:
        if x > y:
            return False
    return True

# 재귀함수
def dfs(depth, num):
    global answer
    # 숫자 자리수를 만족했다면,
    if depth == k + 1:
        answer.append(num)
        return

    for i in range(10):
        if not visited[i]:
            #depth가 0이면 문자열에 넣어주고, 아니면 부등호 만족하는 함수 확인
            if depth == 0 or check(num[depth - 1], str(i), arr[depth - 1]):
                visited[i] = True
                dfs(depth + 1, num + str(i))
                visited[i] = False

k = int(input())
arr = list(map(str, input().split()))

visited = [False] * 10
answer = []
dfs(0, '')
print(max(answer))
print(min(answer))