# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
days, num = map(int, input().split())
inputs = list(map(int, input().split()))

sum_list = [0]
cur = 0
for i in range(len(inputs)):
	cur += inputs[i]
	sum_list.append(cur)
	
for i in range(num) :
	start, end = map(int, input().split())
	result = sum_list[end]- sum_list[start-1]
	ans = '+' + str(result) if result > 0 else result
	print(ans)
	
