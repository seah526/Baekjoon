from math import prod

def mult(num_list) :
    ans = 1
    for i in num_list :
        ans *= i
    return ans

def solution(num_list):
    # return sum(num_list) if (len(num_list) >= 11) else mult(num_list)

    return sum(num_list) if (len(num_list)>= 11) else prod(num_list)