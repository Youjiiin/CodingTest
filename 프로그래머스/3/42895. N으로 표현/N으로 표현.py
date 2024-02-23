def solution(N, number):
    answer = -1
    dp = []
    
    for i in range(1, 9):
        case = set()
        check_num = int(str(N) * i)
        #{N} {NN} ..
        case.add(check_num)
        
        for j in range(i - 1):
            for op1 in dp[j]:
                for op2 in dp[-j-1]:
                    case.add(op1 + op2)
                    case.add(op1 - op2)
                    case.add(op1 * op2)
                    if op2 != 0:
                        case.add(op1 // op2)
                        
        if number in case:
            answer = i
            break
            
        dp.append(case)
    return answer