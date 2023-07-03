def solution(dots):
    x = set([dots[0][0], dots[1][0], dots[2][0], dots[3][0]])
    y = set([dots[0][1], dots[1][1], dots[2][1], dots[3][1]])
    
    x1, x2 = x.pop(), x.pop()
    y1, y2 = y.pop(), y.pop()
    
    return abs(x1 - x2) * abs(y1 - y2)