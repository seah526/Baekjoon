T = int(input())

for t in range(T):
    sent = input().split()
    ans = ' '.join(i[-1::-1] for i in sent)
    print(ans)