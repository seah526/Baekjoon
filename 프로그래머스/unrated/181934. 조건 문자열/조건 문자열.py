def solution(ineq, eq, n, m):
    if eq == '=' : 
        answer = str(n) + ineq + eq + str(m)
    else :
        answer = str(n) + ineq + str(m)
    return int(eval(answer))