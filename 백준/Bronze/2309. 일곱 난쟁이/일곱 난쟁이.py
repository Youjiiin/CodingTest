from itertools import permutations
height = []
for _ in range(9):
    height.append(int(input()))

for i in permutations(height, 2):
    h_list = height.copy()
    h_list.remove(i[0])
    h_list.remove(i[1])

    if sum(h_list) == 100:
        for j in sorted(h_list):
            print(j)
        break