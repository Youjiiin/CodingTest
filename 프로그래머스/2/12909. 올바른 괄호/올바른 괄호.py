def solution(s):
    answer = [0, 0]
    for i in range(len(s)):
        if s[i] == "(":
            answer[0] += 1
        else:
            answer[1] += 1
        if answer[0] < answer[1]:
            return False
        
    if answer[0] == answer[1]:
            return True
    else:
            return False