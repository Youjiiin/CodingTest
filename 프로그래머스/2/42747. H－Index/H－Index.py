def solution(citations):
    #논문 n편 중, a번 이상 인용된 논문이 b편 이상이면 a 와 b중 작은 값이 hIndex 값입니다.
    answer = 0
    citations.sort(reverse=True)
    print(citations)
    for i in range(len(citations)):
        if i >= citations[i]:
            return i
    
    return len(citations)