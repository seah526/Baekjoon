def solution(keyinput, board):
    
    input = {"left" : [-1, 0], "right": [1, 0], "up" : [0, 1], "down" : [0, -1]}
    answer = [0, 0]
    limit_x, limit_y = board[0]//2, board[1]//2
    
    for key in keyinput :
        temp_x = answer[0] + input[key][0]
        temp_y = answer[1] + input[key][1]
        
        if limit_x >= abs(temp_x) :
            answer[0] = temp_x
        if limit_y >= abs(temp_y): 
            answer[1] = temp_y 
        
    return answer