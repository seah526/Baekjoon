def solution(strArr):
    answer = [len(i) for i in strArr]
    temp = []
    for i in set(answer) :
        temp.append(answer.count(i))
    return max(temp)