budget = int(input())
chart = list(map(int, input().split()))

# 준현
jun = 0
jun_m = budget
for i in chart:
    jun += jun_m // i
    jun_m = jun_m % i
    if jun_m == 0:
        break

j_total = jun * chart[-1] + jun_m

# 성민
sung = 0
sung_m = budget
for i in range(len(chart) - 4):
    #매도
    if chart[i] < chart[i + 1] < chart[i + 2] < chart[i + 3]:
        sung_m += chart[i + 3] * sung
        sung = 0

    #매수
    if chart[i] > chart[i + 1] > chart[i + 2] > chart[i + 3]:
        sung += sung_m // chart[i + 3]
        sung_m = sung_m % chart[i + 3]

s_total = sung * chart[-1] + sung_m

if j_total > s_total:
    print("BNP")
elif j_total < s_total:
    print("TIMING")
else:
    print("SAMESAME")