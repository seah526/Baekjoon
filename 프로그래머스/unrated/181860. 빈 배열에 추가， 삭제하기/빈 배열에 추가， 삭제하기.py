def solution(arr, flag):
    answer = []
    for idx, x in enumerate(flag) :
        if x:
            answer.extend([arr[idx]]*arr[idx]*2)
        else :
            ans = len(answer) - arr[idx]
            answer = answer[:ans]
    return answer