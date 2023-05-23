def solution(num_list):
    answer = num_list
    last = num_list[len(num_list)-1]
    before = num_list[len(num_list)-2]
    answer.append(last-before if last > before else last*2)
    return answer