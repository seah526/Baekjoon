def solution(arr):
    power = 1
    while power - len(arr) < 0:
        power *= 2
    return arr + [0] * (power - len(arr))