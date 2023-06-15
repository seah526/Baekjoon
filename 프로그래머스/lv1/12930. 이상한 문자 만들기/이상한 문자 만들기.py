def solution(s):
    
    # answer = ''
    # count = 0
    # for a in s :
    #     if a == ' ':
    #         count = 0
    #         answer += a
    #     else :
    #         if count % 2 :
    #             answer += a.lower()
    #         else :
    #             answer += a.upper()
    #         count += 1
    # return answer
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
