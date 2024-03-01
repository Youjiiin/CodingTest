def solution(n, lost, reserve):
    # 잃어버린 학생 - 여벌 옷을 가지고 있는 학생이 바로 옆 번호인지 확인
    # [2, 4] [3]인 경우, 한 명은 빌려주고 한 명은 못 빌려줌
    reserve.sort()
    lost.sort()
    # 잃어버렸는데 여벌이 있는 경우
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)

    # 옆 사람이 여벌있는지 확인
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)


    return n - len(lost)