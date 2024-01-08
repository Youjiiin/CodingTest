hour, minute = map(int, input().split())
time = int(input())

hour += int(time // 60) # 시간단위
minute += int(time % 60) # 분단위

if minute >= 60:
    hour += 1
    minute -= 60
if hour >= 24:
    hour -= 24

print(hour, minute)