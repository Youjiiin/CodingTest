def solution(arr):
    result = []
    result.append(arr[0])
    for i in range(1, len(arr)):
        if result[-1] == arr[i]:
            continue
        else:
            result.append(arr[i])
        
    return result