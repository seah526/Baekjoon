def solution(s):
    answer = 0
    
    for i in s :
        if i == '(':
            answer += 1
        elif i == ')' and answer > 0:
            answer -= 1
        else :
            return False 
        
    if answer :
        return False
    else :
        return True
