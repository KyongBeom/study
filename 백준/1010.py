import math
N = int(input())

for i in range(N):
    A, B = map(int,input().split())
    X = math.factorial(A)
    Y = math.factorial(B)
    Z = math.factorial(B-A)

    ans = Y//(Z*X)
    print(ans)

