def solution(n):
    answer = []
    num = n
    while num != 1 :
        answer.append(num)
        if num % 2 :
            num = 3 * num + 1
        else :
            num //= 2
    answer.append(1)
    
    return answer