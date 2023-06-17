def solution(orders):
    answer = 0
    for order in orders : 
        if 'cafelatte' in order :
            answer += 1
    return answer * 500 + len(orders) * 4500