def solution(nums):
    # 고르려는 폰켓몬 마리수
    num = len(nums) // 2
    nums = set(nums)
    
    # 가질 수 있는 종류의 개수를 반환해야한다.
    # 최대는 N / 2
    if len(nums) < num:
        answer = len(nums)
    else:
        answer = num
    
    return answer