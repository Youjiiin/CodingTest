import heapq

# 힙큐로 가장 안매운 + 두번째로 안매운 계산 진행
# K이상은 모두 큐에서 빼버릴까
def solution(scoville, K):
    count = 0
    heap = []
    
    # K이하의 음식들만 큐에 삽입
    for i in scoville:
        heapq.heappush(heap, i)
         
    # 모든 요소가 K이상이 될때까지 진행
    while heap[0] < K:
        # 음식 섞기
        heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        # 카운트 증가
        count += 1
        
        if len(heap) == 1 and heap[0] < K:
            return -1

    return count