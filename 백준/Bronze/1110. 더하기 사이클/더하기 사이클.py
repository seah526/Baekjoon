N = int(input())

cnt=0
num = 0
cur = N
if N == 0:
    print(1)
else :
    while num != N :
        num = (cur%10) * 10 + (cur//10 + cur%10) % 10
        cur = num
        cnt += 1

    print(cnt)