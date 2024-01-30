def solution(numbers):
    numbers_str = [str(num) for num in numbers]
    numbers_str.sort(key=lambda num: num*3, reverse=True) 
    
    # 0이 연속해서 나오는 것을 없애기 위한 int -> str
    return str(int(''.join(numbers_str)))