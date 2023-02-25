import re

def solution(my_string):
    answer = 0
    numbers = re.findall(r'\d+', my_string)

    return sum(int(i) for i in numbers)