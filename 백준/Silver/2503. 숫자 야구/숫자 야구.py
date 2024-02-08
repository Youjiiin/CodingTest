from itertools import permutations

num_list = list(permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3))

time = int(input())
for _ in range(time):
    q, strike, ball = map(int, input().split())
    q = list(str(q))
    removed = 0

    for i in range(len(num_list)):
        count_strike, count_ball = 0, 0
        i -= removed

        # 각각 숫자 확인
        for j in range(3):
            if q[j] == num_list[i][j]:
                count_strike += 1
            elif q[j] in num_list[i]:
                count_ball += 1
        
        if count_strike != strike or count_ball != ball:
            num_list.remove(num_list[i])
            removed += 1

print(len(num_list))
