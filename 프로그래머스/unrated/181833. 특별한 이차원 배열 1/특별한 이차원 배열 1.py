def solution(n):
    answer = []
    for i in range(n) :
        item = [0] * n
        item[i] = 1
        answer.append(item)
    return answer