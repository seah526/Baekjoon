def solution(rsp):
    ans = ""
    for i in rsp:
        if i == "2" : 
            ans += "0"
        elif i == "5" :
            ans += "2"
        else :
            ans += "5"
    return ans