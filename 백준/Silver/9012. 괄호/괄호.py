t = int(input())
for _ in range(t):
    string = input()
    open = 0
    result = "YES"

    for i in range(len(string)):
        if string[i] == '(':
            open += 1
        elif string[i] == ")":
            if open == 0:
                result = "NO"
                break
            else:
                open -= 1
    
    if open == 0:
        print(result)
    else:
        print("NO")