def solution(s):
    s = s.lower()
    answer = ''
    if s[0].isalpha() :
        answer += s[0].upper()
    else :
        answer += s[0]
    
    for idx in range(1, len(s)):
        if s[idx-1] == ' ' and s[idx].isalpha():
            answer += s[idx].upper()
        else :
            answer += s[idx]

    return answer