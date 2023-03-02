numbers = []

for i in range(7):
    temp = int(input())
    if temp %2 == 1:
        numbers.append(temp)

if len(numbers) == 0:
    print(-1)
else :
    print(sum(numbers), min(numbers), sep='\n')