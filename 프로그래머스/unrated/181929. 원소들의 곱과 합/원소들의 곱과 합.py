from math import prod
def solution(num_list):
    return int(prod(num_list) < sum(num_list)**2)