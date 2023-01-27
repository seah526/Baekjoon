def solution(price, money, count):
    

    return (sum(range(count+1))*price - money) if (sum(range(count+1))*price - money) > 0 else 0