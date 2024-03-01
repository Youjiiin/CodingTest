from collections import deque
def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    q = deque()
    q.append((begin, 0))
    visited = [False] * len(words)
    
    while q:
        w, count = q.popleft()
        
        if w == target:
            answer = count
            break
        
        for i in range(len(words)):
            dif = 0
            if not visited[i]:
                for j in range(len(w)):
                    if words[i][j] != w[j]:
                        dif += 1
                    
                if dif == 1:
                    visited[i] = True
                    q.append((words[i], count + 1))
        
    return answer