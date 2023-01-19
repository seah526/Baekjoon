def solution(x):
    cnt = sum(int(i) for i in str(x))
    return x%cnt==0