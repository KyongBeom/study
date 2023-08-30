import math

N = int(input())

K = int((1+math.sqrt(4*1*2*N-1))//(2*1))
index = 0

for i in range(K+1):
    index += i

check = index - N
if K%2:
    top = check + 1
    bottom = K - check
else:
    top = K - check
    bottom = check + 1

print(str(top) + "/" + str(bottom))