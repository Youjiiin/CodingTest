def solution(phone_book):
    answer = True
    # 각 인덱스로 돌아가면서 in -> 가운데 있어도 인식됨
    # 맨 앞에 있는걸 확인하는 방법?
    # 접두사일때, 더 작은 값의 길이만큼 돌아보며 a[i] == b[i] 이면 false
    # 리스트에서 서로다른 두개의 요소를 비교하는 방법에는 뭐가 있을까?
    # 이중 for문인데 이는 너무 오래걸림.
    
    # 문자열 값을 sort하면 숫자 크기 순이 아닌, 각 유니코드 값에 의해 정렬된다.
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            answer = False
            break
    
    return answer