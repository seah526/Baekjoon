# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = int(input())

for i in range(user_input):
	x, y, n = map(int, input().split())
	move = abs(x) + abs(y)

	if (move <= n) and ((n-move) % 2 ==0):
		print('YES')
	else :
		print('NO')
