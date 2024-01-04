def solution(players, callings):
    rank = {}
    name = {}
    
    for i in range(len(players)):
        rank[players[i]] = i # 등수 value
        name[i] = players[i] # 이름 value
    
    for i in callings:
        win = rank[i] # 불린사람 등수 호출
        rank[i] = win - 1 # 불린 사람 등수 올리기 계산
        
        p = name[win - 1] # 추월당한사람 이름
        rank[p] = win # 추월당한사람 등수 가져오기
        
        name[win - 1] = i # 추월자 등수 올려주기
        name[win] = p # 추월당한 사람 등수 내리기

    return list(name.values())