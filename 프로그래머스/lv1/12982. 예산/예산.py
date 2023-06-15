def solution(d, budget):
    answer = 0
    
    for idx, a in enumerate(sorted(d)) : 
        answer += a
        print(idx, a, answer)
        if answer > budget :
            return idx 
        else :
            pass
    return len(d)