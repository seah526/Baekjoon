def solution(bin1, bin2):
    # res = int(bin1, 2) + int(bin2, 2)
    # ans = ''
    # while res > 0 :
    #     ans += str(res%2)
    #     res //= 2
    # return ans[::-1]
    return bin(int(bin1, 2) + int(bin2, 2))[2:]