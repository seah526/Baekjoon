N = int(input())

ans = list(map(int, input().split()))
result = [0 for i in range(N)]

result[0] = ans[0]
for idx in range(1, N):
    if ans[idx] == 0:
        result[idx] = 0
    else :
        result[idx] = (result[idx-1] + 1)
print(sum(result))
   