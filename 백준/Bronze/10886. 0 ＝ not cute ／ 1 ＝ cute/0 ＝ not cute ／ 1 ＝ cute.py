N = int(input())

cnt = 0
for i in range(N):
    if int(input()) == 1:
        cnt += 1
    
print("Junhee is not cute!" if cnt <= N//2 else "Junhee is cute!")