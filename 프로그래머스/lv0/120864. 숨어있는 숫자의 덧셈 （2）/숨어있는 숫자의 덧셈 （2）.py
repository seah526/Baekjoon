import re

def solution(my_string):
    answer = 0
    numbers = re.findall(r'\d+', my_string)

    return sum(int(i) for i in numbers)

def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())