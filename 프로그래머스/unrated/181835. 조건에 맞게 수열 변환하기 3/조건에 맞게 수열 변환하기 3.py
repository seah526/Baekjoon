def solution(arr, k):
#     answer = []

#     if k % 2 :
#         for i in arr :
#             answer.append(i*k)
#     else :
#         for i in arr :
#             answer.append(i+k)
#     return answer

    return [i*k if k%2 else i+k for i in arr]