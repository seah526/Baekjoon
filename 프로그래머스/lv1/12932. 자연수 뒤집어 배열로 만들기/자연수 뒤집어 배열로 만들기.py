def solution(n):
    answer = []
    while n > 0 :
        answer.append(n%10)
        n //= 10
    return answer

# def digit_reverse(n):
#     return [int(i) for i in str(n)][::-1]

# def digit_reverse(n):
#     return list(map(int, reversed(str(n))))