def solution(n):
    return [i*2+1 for i in range(n//2+n%2)]
    # return [i for i in range(1, n+1, 2)]