def solution(numbers, k):
    answer = 1
    for i in range(1,k):
        answer = (answer + 2) % len(numbers)

    if answer == 0 :
        answer = len(numbers)
    return answer