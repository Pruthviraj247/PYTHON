class A:
    X = "Hey I Am X variable of Class A"

    def __init__(self):
        self.X1 = "I Am Inside of Function of class A"

class B(A):
    Y = "Hey I Am In Class B"

# P = A()
# print(P.X)
Q = B()

print(Q.Y)
