D1 = {X:X*2 for X in range(10)}
# print(D1)

D2 = {X:X*2 for X in range(10) if X%2==0}
print(D2)
#
D3 = {X:X*2 for X in range(10) if X%2==0 if X%3==0}
# print(D3)

D4 = {X:(X if X%2==0 else 'Skiped' ) for X in range(10)}
print(D4)
