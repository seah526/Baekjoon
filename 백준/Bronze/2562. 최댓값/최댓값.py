numbers = list(int(input()) for i in range(9))

print(max(numbers), numbers.index(max(numbers))+1, sep='\n')
