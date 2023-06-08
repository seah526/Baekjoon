def solution(arr, queries):
    for first, second in queries :
        arr[first], arr[second] = arr[second], arr[first]
    return arr