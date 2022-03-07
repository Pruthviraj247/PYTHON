D1 = {}

for X in range(10):
    D1[X] = X*2
print(D1)

D2 = {}

for Y in range(10):
    if(Y%2==0):
        D2[Y] = Y*2
# print(D2)

D3 = {}

for Z in range(100):
    if(Z%2==0):
        if(Z%3==0):
            D2[Z] = Z*2
print(D3)
