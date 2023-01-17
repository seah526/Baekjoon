def solution(s1, s2):
    return len([i for i in s1 if i in s2]) 
    # answer = 0
    # for element in s1 :
    #     if element in s2:
    #         answer += 1
    # return answer

# def solution(s1, s2):
#     return len(set(s1)&set(s2));