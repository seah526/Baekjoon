# a, b = map(int, input().strip().split(' '))
# for i in range(b):
#     for k in range(a):
#         print("*", end="")
#     print()

a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)