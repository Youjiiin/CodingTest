import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
num = list(map(int, input().split()))

dic = {}

for i in num:
    dic[i] = 0

for i in card:
    if i in dic:
        dic[i] = 1

for i in dic:
    print(dic[i], end = " ")