n = int(input())
card = list(map(int, input().split()))
card.sort()

gold = 0
for i in range(0, n - 1):
    gold += card[-1] + card[i]
print(gold)