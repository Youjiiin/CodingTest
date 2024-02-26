from collections import deque
n = list(input().strip())
q = deque()
result = []
tag = False

for i in n:
    if i == '<':
        tag = True
        while q:
            result.append(q.pop())
    elif i == '>':
        tag = False
        result.append('<'+''.join(q)+'>')
        q.clear()
    elif tag:
        q.append(i)

    else:
        if i == ' ':
            while q:
                result.append(q.pop())
            result.append(' ')
            q.clear()
        else:
            q.append(i)

while q:
    result.append(q.pop())

print(''.join(result))