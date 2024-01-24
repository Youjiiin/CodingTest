def solution(participant, completion):
    answer = ''
    # 동명이인이 있을 수 있으므로 in을 쓰면 안될 것 같음
    # 인덱스 값으로?
    # 없는 인덱스 값으로 찾아서 출력하면 되려나
    # 완주한 사람 대로 정렬할 수 있는 방법은 없나 -> 빡센듯
    # 참가자 명단의 각 값을 카운트? -> 시간초과
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    if len(answer) == 0:
        answer = participant[-1]
    return answer