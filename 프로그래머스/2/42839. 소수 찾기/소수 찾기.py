from itertools import permutations

# 소수확인 함수
def is_snum(x):
    if x < 2 :
        return False
    
    for i in range(2, x) :
        if x % i == 0 :
            return False
            
    return True

def solution(numbers):
    answer = 0
    nums = []
    
    # 각각 조합하기
    for i in range(1, len(numbers)+1) :
        nums.append(list(set(map(''.join, permutations(numbers, i)))))
    per = list(set(map(int, set(sum(nums, [])))))
    
    for p in per:
        if is_snum(p) == True:
            answer += 1

    return answer