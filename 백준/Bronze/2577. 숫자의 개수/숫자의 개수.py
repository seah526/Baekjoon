A = int(input())
B = int(input())
C = int(input())

sum = A * B * C

for i in range(10):
    print(str(sum).count(str(i)))
