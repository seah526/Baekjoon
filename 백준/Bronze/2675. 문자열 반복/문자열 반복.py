T = int(input())

for t in range(T):
    n, word = input().split()
    ans = ''
    for i in word:
        ans += i*int(n)

    print(ans)