l, c = map(int, input().split())
words = input().split()
m = ['a', 'e', 'i', 'o', 'u']

words.sort()

def check(arr):
    count_m = 0
    count_not_m = 0
    for i in arr:
        if i in m:
            count_m += 1
        else:
            count_not_m += 1
    if count_m >= 1 and count_not_m >= 2:
        return True
    else:
        return False

def backtracking(arr):
    if len(arr) == l:
        if check(arr):
            print("".join(arr))
            return
        
    for i in range(len(arr), c):
        if arr[-1] < words[i]:
            arr.append(words[i])
            backtracking(arr)
            arr.pop()

for i in range(c - l + 1):
    arr = [words[i]]
    backtracking(arr)