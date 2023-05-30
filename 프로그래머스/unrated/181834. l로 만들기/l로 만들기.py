def solution(myString):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    answer = ''
    for a in myString :
        if a in alpha :
            answer += 'l'
        else :
            answer += a
    
    return answer