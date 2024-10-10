name = input()

count = dict()
keys = sorted(list(set(name)))
odd = []

# 각 글자가 몇개 씩 있는지 - 홀수 개있는 글자가 몇갠지
for k in keys:
    cnt = name.count(k)
    count[k] = cnt

    if cnt % 2:
        odd.append(k)

# 홀수 개수인 글자가 2개 이상이라면 안됨
if len(odd) > 1:
    print("I'm Sorry Hansoo")
else:
    result = ''

    for key in keys:
        result += key * (count[key] // 2)

    if odd:
        result += odd[0] + result[::-1]
    else:
        result += result[::-1]

    print(result)