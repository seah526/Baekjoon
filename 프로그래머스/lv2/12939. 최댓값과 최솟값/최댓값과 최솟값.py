def solution(s):
    # a = s.split()
    # a = list(map(int, a))
    a = list(map(int,s.split()))
    return f"{min(a)} {max(a)}"