def solution(n, t):
    ans = n
    for i in range(t):
        ans *= 2
    return ans
# return n*(2**t)