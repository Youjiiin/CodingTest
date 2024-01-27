def solution(name):
    #각 알파벳을 얼만큼 이동시켜야 해당 알파벳으로 변경되는지 확인
    #뒤로 이동하는 편이 빠를 수 있다. -> 어떻게 판단할 것인가
    #각 알파벳의 위치에 따라 버튼을 눌러야한다. 
    #어떻게 이동해야 최소한으로 이동할 수 있는가?
    #다음에 A가 있다면 뒤로 이동하는 편이 빠른가?
    answer = 0
    min_move = len(name) - 1 # 그냥 순서대로 변경했을 때
    
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        # A는 안움직여도 되지만, Z는 한번은 움직여야 하므로.
        
        # 다음 글자로 이동
        next = i + 1
        # A가 나오는데 찾기
        while next < len(name) and name[next] == 'A':
            next += 1
        min_move = min(min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next))
        
    answer += min_move
    return answer