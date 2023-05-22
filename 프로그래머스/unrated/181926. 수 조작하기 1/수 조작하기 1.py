def solution(n, control):
    dics = {"w" : 1, "s": -1, "d": 10, "a": -10}
    for i in control :
        n += dics[i]
    return n