def solution(numLog):
    answer = ''
    dics = {+1: 'w', -1: 's', +10: 'd', -10 : 'a'}
    
    for idx in range(len(numLog)-1):
        cur = numLog[idx + 1] - numLog[idx]
        answer += dics[cur]
        
    return answer