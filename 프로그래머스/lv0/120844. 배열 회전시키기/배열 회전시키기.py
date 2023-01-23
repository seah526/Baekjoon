def solution(numbers, direction):
    answer = []
    if direction == 'left':
        for idx, i in enumerate(numbers) :
            answer.insert((idx-1)%len(numbers), i)
    else :
        for idx, i in enumerate(numbers):
            answer.insert((idx+1)%len(numbers), i)
    return answer