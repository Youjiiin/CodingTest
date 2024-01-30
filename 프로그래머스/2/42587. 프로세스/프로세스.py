from collections import deque
def solution(priorities, location):
    q = deque(priorities)
    answer = 0
    while q:
        max_p = max(q)
        now = q.popleft()
        location -= 1
        
        if max_p != now:
            q.append(now)
            if location < 0:
                location = len(q) - 1
        else:
            answer += 1
            if location < 0:
                break
                
    return answer