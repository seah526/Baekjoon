word = input()

length = len(word) // 10 

for l in range(length+1):
    print(word[10*l:10*(l+1)])