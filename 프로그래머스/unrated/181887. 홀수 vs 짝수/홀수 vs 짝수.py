def solution(num_list):
    odd = sum(num_list[i] for i in range(1, len(num_list), 2))
    even = sum(num_list) - odd
    return max(odd, even)