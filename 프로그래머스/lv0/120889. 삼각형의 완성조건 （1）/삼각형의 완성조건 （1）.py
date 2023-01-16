def solution(sides):
    sides.sort()
    answer = 1 if (sides[0] + sides[1] > sides[2] ) else 2
    
    return answer

    # return 1 if max(sides) < (sum(sides) - max(sides)) else 2