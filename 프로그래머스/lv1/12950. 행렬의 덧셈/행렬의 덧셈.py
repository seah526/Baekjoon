def solution(arr1, arr2):
    answer = []
    column = len(arr1)
    row = len(arr1[0])
    
    for i in range(column) :
        temp = []
        for j in range(row) :
            temp.append(arr1[i][j]+arr2[i][j])
        answer.append(temp)
    return answer