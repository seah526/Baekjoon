dic = {"č": "c=", 
        "ć" : "c-", 
        "dž" : "dz=", 
        "đ" : "d-", 
        "lj" : "lj", 
        "nj" : "nj", 
        "š" : "s=", 
        "ž" : "z="}

word = input()

cnt = 0
for i in dic.items() :
    if i[1] in word :
        cnt += word.count(i[1])

print(len(word)- cnt)