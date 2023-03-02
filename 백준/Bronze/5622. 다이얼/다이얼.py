numbers = {
    'ABC' : 2,
    'DEF' : 3,
    'GHI' : 4,
    'JKL' : 5,
    'MNO' : 6,
    'PQRS' : 7,
    'TUV' : 8,
    'WXYZ' : 9
}

words = input()
times = len(words)
for i in words :
    for key in numbers.keys() : 
        if i in key :
            times += numbers[key]

print(times)