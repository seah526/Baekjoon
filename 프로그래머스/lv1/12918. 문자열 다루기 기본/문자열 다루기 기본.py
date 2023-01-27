def solution(s):
    # if len(s) == 4 or len(s) == 6:
    #     for i in s:
    #         if not i.isdigit():
    #             return False
    #     return True
    # else :
    #     return False
    return len(s) in (4,6) and s.isdigit()