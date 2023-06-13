def solution(my_string, indices):
    answer = ''
    for idx, i in enumerate(my_string) :
        if idx in indices :
            pass
        else :
            answer += i
    return answer