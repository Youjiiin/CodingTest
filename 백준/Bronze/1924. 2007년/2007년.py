month, day = map(int, input().split())
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d = 0

for i in range(month - 1):
    d += arr[i]
d += day
w = d % 7
print(week[w])