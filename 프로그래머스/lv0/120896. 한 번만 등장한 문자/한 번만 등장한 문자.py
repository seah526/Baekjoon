def solution(s):
    dic = {}
    for i in sorted(s):
        if i in dic.keys() :
            dic[i] += 1
        else :
            dic[i] = 1
            
    return ''.join(i[0] for i in dic.items() if i[1] == 1)