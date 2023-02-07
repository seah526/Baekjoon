from collections import OrderedDict

def solution(my_string):
    # return ''.join(OrderedDict.fromkeys(my_string))
    ans = ''
    for i in my_string :
        if i not in ans :
            ans += i
        else :
            continue
    return ans