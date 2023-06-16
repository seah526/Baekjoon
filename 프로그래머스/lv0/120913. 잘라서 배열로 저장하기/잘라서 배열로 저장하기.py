def solution(my_str, n):
    answer = []
    idx = 0
    limit = len(my_str)
    while idx < len(my_str) :
        answer.append(my_str[idx:min(idx+n, limit)])
        idx += n
    return answer
