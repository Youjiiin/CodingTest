from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    now_weight = 0
    
    while bridge:
        # 시간증가
        answer += 1
        # 현재 다리 위의 무게 - 다리위의 자동차 무게
        now_weight -= bridge.popleft()
        
        # 뒤에차와의 합이 10이 넘는다면, 앞 차가 다 지나갈때 까지 기다려야함
        # 뒤에 차와의 합이 10이 안되면, 바로 다음차 투입
        if q:
            if now_weight + q[0] <= weight:
                truck = q.popleft()
                bridge.append(truck)
                now_weight += truck
            else:
                bridge.append(0)

    return answer