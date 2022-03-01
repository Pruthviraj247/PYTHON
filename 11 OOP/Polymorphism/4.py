class A:
    X = "Hey I Am X variable of Class A"

    def __init__(self):
        self.X1 = "I Am Inside of Function of class A"
        self.X = "I Am Inside of Function"

class B(A):
    X = "Hey I Am In Class B"
    def __init__(self):
        self.X1 = "I Am Inside of Function of class B"
        self.X = "I Am Inside of Function of B"

P = A()
Q = B()

print(P.X)
