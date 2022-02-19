from array import *
A = 3
B = 4
N = A,B

if N < 2:
    print("Not A Prime")
else:
    for i in range(2, N):
        if N%i == 0:
            print("Not A Prime Number")
            break
    else:
        print("Prime Number")
        