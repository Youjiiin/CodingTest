num_list = []
for i in range(1, 10):
    a = int(input())
    num_list.append(a)
m = max(num_list)

print(m)
print(num_list.index(m) + 1)