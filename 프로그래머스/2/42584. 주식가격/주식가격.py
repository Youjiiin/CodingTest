def solution(prices):
    answer = []
    #다음 값이 나보다 크면 count += 1
    #다음 값이 나보다 작으면 더하지 않음
    for i in range(len(prices)):
        count = 0
        for j in range(i+1, len(prices)):
            count += 1
            if prices[i] > prices[j]:
                break
        answer.append(count)
        
    return answer