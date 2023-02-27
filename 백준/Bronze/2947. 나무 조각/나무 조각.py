numbers = list(map(int, input().split()))

while True :
    for i in range(4):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            print(*numbers, sep=' ')
        
    if sorted(numbers) == numbers :
        break