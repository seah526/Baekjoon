def solution(arr, divisor):
    ans = sorted([i for i in arr if i%divisor==0]) 
    if len(ans) < 1 :
        ans = [-1]
    return ans