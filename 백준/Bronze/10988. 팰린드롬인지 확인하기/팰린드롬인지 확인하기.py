word = input()

for i in range(len(word)//2):
    if word[i] == word[-(i+1)] :
        pass
    else :
        print(0)
        break
else :
    print(1)
