def solution(n):
    num = 1
    i = 1
    while True:
        if num * i < n :
            num *= i
            i += 1
        elif num*i == n:
            return i
        else : 
            return i - 1
        