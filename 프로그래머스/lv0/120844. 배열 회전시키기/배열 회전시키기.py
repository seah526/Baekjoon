def solution(numbers, direction):
    answer = []
    if direction == 'left':
        for idx, i in enumerate(numbers) :
            answer.insert((idx-1)%len(numbers), i)
    else :
        for idx, i in enumerate(numbers):
            answer.insert((idx+1)%len(numbers), i)
    return answer
    # return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]
