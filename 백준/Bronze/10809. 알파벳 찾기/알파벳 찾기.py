word = input()
ans = []

for i in range(ord('a'), ord('z')+1) : 
    ans.append(word.find(chr(i)))

for i in ans :
    print(i, sep = ' ')