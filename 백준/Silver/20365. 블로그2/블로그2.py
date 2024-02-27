n = int(input())
color = list(map(str, input().strip()))
dic = {'B' : 0, 'R' : 0}

dic[color[0]] += 1

for i in range(1, n):
    if color[i] != color[i - 1]:
        dic[color[i]] += 1

result = min(dic['B'], dic['R']) + 1
print(result)