from collections import deque

n = int(input())
q = deque()
for i in range(1, n + 1):
    q.append(i)

for _ in range(n - 1):
    q.popleft()

    if len(q) == 1:
        break
    else:
        num = q.popleft()
        q.append(num)
print(q[0])