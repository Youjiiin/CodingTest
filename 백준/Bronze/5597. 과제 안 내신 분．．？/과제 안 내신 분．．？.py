student = [i for i in range(1, 31)]

for _ in range(1, 29):
    j = int(input())
    student.remove(j)

for a in student:
    print(a)