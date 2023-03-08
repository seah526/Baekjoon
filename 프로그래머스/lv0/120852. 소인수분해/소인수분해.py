def solution(n):
    answer = []
    ans = []
    
    for i in range(2, n+1):
        if n % i == 0:
            answer.append(i)
            
    for k in answer :
        cnt = 0
        for j in range(1, k+1):
            if k % j == 0:
                cnt += 1
        if cnt == 2 :
            ans.append(k)
    return ans