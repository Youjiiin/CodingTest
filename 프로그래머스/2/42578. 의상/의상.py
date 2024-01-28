def solution(clothes):
    #각 종류를 하나씩만 착용하고 시작한다.
    answer = 1
    #종류가 두개 이상이라면, 이후에 다음날에 겹치지 않도록 두개 이상씩 착용
    #1. 입력받은 것을 어떻게 구별할 것인가?
    #key-value -> 딕셔너리는 key값이 같으면 값을 덮어쓴다. 
    closet = {}
    for _, kind in clothes:
        if kind in closet.keys():
            closet[kind] += 1
        else:
            closet[kind] = 1

    for value in closet.values():
        answer *= (value + 1)
    
    return answer - 1