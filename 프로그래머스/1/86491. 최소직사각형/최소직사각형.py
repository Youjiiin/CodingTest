def solution(sizes):
    answer = 0
    max_a = 0
    max_b = 0
    
    for i in sizes:
        i.sort()
        max_a = max(max_a, i[0])
        max_b = max(max_b, i[1])
    answer = max_a * max_b
    return answer