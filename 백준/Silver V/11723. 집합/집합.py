import sys
input = sys.stdin.readline

m = int(input())
s = set()

for _ in range(m):
    x = list(map(str, input().strip().split()))
    if len(x) == 1:
        if x[0] == "all":
            s = set([i for i in range(1, 21)])

        elif x[0] == "empty":
            s = set()
    else:
        if x[0] == "add":
            s.add(int(x[1]))

        elif x[0] == "remove":
            s.discard(int(x[1]))

        elif x[0] == "toggle":
            if int(x[1]) in s:
                s.remove(int(x[1]))
            else:
                s.add(int(x[1]))

        elif x[0] == "check":
            if int(x[1]) in s:
                print(1)
            else:
                print(0)