def solution(num_list, n):
    answer = []
    temp = len(num_list) // n
    for i in range(temp):
        answer.append(num_list[i*n:(i+1)*n])
        
    return answer