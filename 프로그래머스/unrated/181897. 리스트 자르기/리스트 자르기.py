def solution(n, slicer, num_list):
    answer = []
    if n == 1 : 
        b = slicer[1]
        answer = num_list[:b+1]
    elif n == 2 :
        a = slicer[0]
        answer = num_list[a:]
    elif n == 3 :
        a, b = slicer[0:2]
        answer = num_list[a:b+1]
    else :
        a, b, c = slicer
        answer = num_list[a:b+1:c]
    return answer