def solution(arr, divisor):
    print(sorted([i for i in arr if i%divisor==0]))
    # ans = sorted([i for i in arr if i%divisor==0]) 
    # if len(ans) < 1 :
    #     ans = [-1]
    return sorted([i for i in arr if i%divisor==0]) or [-1]