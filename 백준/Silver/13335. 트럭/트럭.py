from collections import deque

n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

time = 0
now = 0

bridge = deque([0] * w)
truck = deque(trucks)

while bridge:
    time += 1
    now -= bridge.popleft()

    if truck:
        if now + truck[0] <= l:
            t = truck.popleft()
            bridge.append(t)
            now += t
        else:
            bridge.append(0)
    
print(time)