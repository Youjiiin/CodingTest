t = int(input())

for _ in range(t):
  n = int(input())
  clothes = {}

  for _ in range(n):
    a, b = map(str, input().split())
    if b in clothes:
      clothes[b] += 1
    else:
      clothes[b] = 1

  result = 1
  for v in clothes.values():
    result *= (v + 1)
  
  print(result - 1)