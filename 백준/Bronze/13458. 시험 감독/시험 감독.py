n = int(input()) # 시험장수
a = list(map(int, input().split())) # 각 시험장의 응시자 수
b, c = map(int, input().split()) # 총 감독관 / 부 감독관이 관리가능인원
cnt = 0

for i in a:
    if i != 0:
        i -= b #총 감독관
        cnt += 1
        if i > 0:
            count = i // c
            cnt += count
            if (i / c) % 1 != 0:
                cnt += 1

print(cnt)