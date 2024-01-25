def solution(array, commands):
    answer = []
    for a in commands:
        arr = array[a[0] - 1 : a[1]]
        arr.sort()
        k = a[2] - 1
        answer.append(arr[k])
    return answer