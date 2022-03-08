D1 = {}

Num = int(input("Enter A Number Of Elements"))

for i in range(Num):
    X = input("Enter Key: ")
    Y = input("Enter Value: ")
    D1.update({X:Y})
print(D1)
