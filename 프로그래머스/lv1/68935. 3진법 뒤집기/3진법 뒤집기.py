def solution(n):
    answer = ''
    i = 1
    res = 0 
    
    while n > 0 :
        answer += str(n % 3)
        n //= 3

    answer = int(answer)
    while answer > 0 :
        res += (answer%10) * i
        answer //= 10
        i *= 3
        
    return res