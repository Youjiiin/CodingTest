s = input()
alpa = "abcdefghijklmnopqrstuvwxyz"

for i in alpa:
    if i in s:
        print(s.index(i), end=" ")
    else:
        print(-1, end=" ")