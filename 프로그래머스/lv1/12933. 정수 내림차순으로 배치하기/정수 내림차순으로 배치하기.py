def solution(n):
    nums = list(int(i) for i in str(n))
    nums.sort(reverse=True)
    answer = 0
    for i in nums :
        answer = answer*10+ i
    return answer