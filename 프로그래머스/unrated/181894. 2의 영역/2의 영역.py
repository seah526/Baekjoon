def solution(arr):
    answer = []
    
    if arr.count(2) >= 2 :
        for idx, i in enumerate(arr):
            if i == 2:
                answer.append(idx)
        return arr[answer[0]:answer[-1]+1]
    elif arr.count(2) == 1 :
        return [2]
    else :
        return [-1]
