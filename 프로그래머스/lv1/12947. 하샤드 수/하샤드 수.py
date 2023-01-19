def solution(x):
    cnt = sum(int(i) for i in str(x))
    return False if x%cnt else True