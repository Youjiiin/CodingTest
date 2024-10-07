k, n = map(int, input().split())
lan = list(int(input()) for _ in range(k))

# 몇개 나오는지 확인
def cut(length):
    count = 0

    for i in lan:
        count += i // length
    return count

result = 0
start = 1
end = max(lan)

while start <= end:
    mid = (start + end) // 2
    if cut(mid) >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)