from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    q = deque()
    q.append((begin, 0))
    
    while q:
        w, step = q.popleft()
        
        if w == target:
            answer = step
            break
        
        for i in words:
            count = 0
            for j in range(len(w)):
                if w[j] != i[j]:
                    count += 1
            if count == 1:
                q.append((i, step + 1))
    
    return answer