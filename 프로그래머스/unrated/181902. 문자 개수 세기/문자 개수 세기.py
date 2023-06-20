def solution(my_string):
    answer = [0] * 52
    
    for i in my_string :
        if i.islower() :
            idx = ord(i) - 71
            answer[idx] += 1
        else :
            idx = ord(i) - 65
            answer[idx] += 1
    return answer