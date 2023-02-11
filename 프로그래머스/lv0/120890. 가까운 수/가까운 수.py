def solution(array, n):
    array.sort()
    ans = [abs(i-n) for i in array]
    print(ans.index(min(ans)))
    return array[ans.index(min(ans))]