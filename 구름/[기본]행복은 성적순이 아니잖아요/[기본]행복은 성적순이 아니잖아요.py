# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
t = int(input())
# print ("Hello Goorm! Your input is " + user_input)
for i in range(t) :
	user_input = list(map(int, input().split()))
	l, s, n, k, m = user_input[0:5]
	scores = user_input[-k:]
	percent = l / 100 * n
	if s < percent : 
		if min(scores) < m :
			print('0')
			break
	else :
		print('0')
		break
		
else :
	print('1')
