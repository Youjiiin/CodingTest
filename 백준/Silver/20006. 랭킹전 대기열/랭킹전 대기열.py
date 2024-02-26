p, m = map(int, input().split())
rooms = []

for i in range(p):
    l, n = input().split()
    l = int(l)

    if not rooms:
        rooms.append([[l, n]])
        continue
    
    # 큐를 잡을 수 있는가
    enter = False
    for room in rooms:
        if len(room) < m and abs(l - room[0][0]) <= 10:
            room.append([l, n])
            enter = True
            break

    if not enter:
        rooms.append([[l, n]])

for room in rooms:
    room.sort(key=lambda x:x[1])

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    for l, n in room:
        print(l, n)   