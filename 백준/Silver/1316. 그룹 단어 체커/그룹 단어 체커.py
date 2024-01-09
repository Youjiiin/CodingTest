num = int(input())
cnt = num

for _ in range(num):
    s = input()
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            pass
        elif s[i] in s[i + 1:]: # arr[i:] i이후의 요소 검사
            cnt -= 1
            break
print(cnt)