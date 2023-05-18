from math import prod

user_input = input()
cur = user_input
ans = []

for idx, i in enumerate(user_input) :
  ans.append(prod(int(k) for k in str(cur)))
  digit = 10 ** (idx+1)
  cur = (int(cur)//digit) * digit -1
  if cur < 0 :
    break
    
print(max(ans))
