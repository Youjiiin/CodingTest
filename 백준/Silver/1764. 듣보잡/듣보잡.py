n, m = map(int, input().split())
listen = [input() for _ in range(n)]
watch = set(input() for _ in range(m))
answer = []

for person in listen:
    if person in watch:
        answer.append(person)

answer.sort()
print(len(answer))
for i in answer:
    print(i)