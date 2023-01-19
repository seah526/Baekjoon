def solution(n, numlist):
    # lst = []
    # for num in numlist :
    #     if num%n == 0:
    #         lst.append(num)
    # return lst
    return list(num for num in numlist if num%n==0 )