from collections import deque

t = int(input())
for _ in range(t):
    p = input() # 명령어
    n = int(input()) # 문자열 개수
    arr = input() # 문자열
    r_flag = 0
    result = []

    if n == 0:
        q = []
    else:
        q = deque(arr[1:-1].split(','))
    
    for i in range(len(p)):
        if p[i] == 'R':
            r_flag += 1
        if p[i] == 'D':
            if len(q) == 0:
                print('error')
                break
            else:
                if r_flag % 2 == 1:
                    q.pop()
                else:
                    q.popleft()
    else:
        if r_flag % 2 == 1:
            q.reverse()
        print('['+','.join(q)+']')