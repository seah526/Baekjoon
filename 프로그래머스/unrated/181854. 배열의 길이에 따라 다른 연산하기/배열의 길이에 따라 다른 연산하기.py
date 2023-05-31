def solution(arr, n):
    answer = []
    if len(arr) % 2 :
        for idx, i in enumerate(arr):
            answer.append(i+n if idx%2==0 else i)
    else :
        for idx, i in enumerate(arr):
            answer.append(i+n if idx%2 else i)
    return answer