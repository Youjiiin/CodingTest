n = input().upper()
s = list(set(n))
count_list = []

for i in s:
    count_list.append(n.count(i))

if count_list.count(max(count_list)) > 1:
    print("?")
else:
    print(s[count_list.index(max(count_list))])