def solution(numbers):
    dics = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for idx, i in enumerate(dics):
        numbers = numbers.replace(i, str(idx))
    return int(numbers) 