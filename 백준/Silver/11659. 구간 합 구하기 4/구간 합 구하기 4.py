import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
sum = [0]
tmp = 0

# 누적합 구하기
for i in num:
    tmp = tmp + i
    sum.append(tmp)

for _ in range(m):
    i, j = map(int, input().split())

    # 시간 복잡도에 의해서 구간 합은 O(1)
    print(sum[j] - sum[i - 1])