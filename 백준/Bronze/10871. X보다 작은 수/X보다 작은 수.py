N, X = map(int, input().split())

lists = list(map(int, input().split()))

ans = [i for i in lists if i<X]

for i in ans :
    print(i, end=' ')