f, s, t = map(int, input().split(" "))
money = 0

if f == s == t :
    money = 10000 + f * 1000
elif f == s :
    money = 1000 + f * 100
elif f == t :
    money = 1000 + f * 100
elif s == t :
    money = 1000 + s * 100
else :
    money = max(f, s, t) * 100
print(money)