def solution(myString, pat):
    answer = 0
    until = len(pat)
    for i in range(len(myString)) : 
        if myString[i:i+until] == pat :
            answer += 1
    return answer