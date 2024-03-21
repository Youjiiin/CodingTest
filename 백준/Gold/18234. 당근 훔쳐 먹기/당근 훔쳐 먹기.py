import sys
input = sys.stdin.readline

n, t = map(int, input().split()) # 종류, t동안 재배
carrot = [list(map(int, input().split())) for _ in range(n)] # 당근의 맛, 영양제
carrot.sort(key = lambda x : x[1], reverse=True)

rabbit = 0 # 토끼가 총 훔쳐먹은 당근 맛 총량
for w, p in carrot:
    rabbit += (w + p * (t - 1))
    t -= 1

print(rabbit)