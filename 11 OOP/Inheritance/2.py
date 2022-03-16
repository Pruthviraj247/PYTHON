class A():
    """This Is Program of Multi-Level Inheritance"""
    def a(self):
        print("This Is A 1st Inheritance")

class B():
    def b(self):
        print("This Is A 2nd Inheritance")

class C():
    def c(self):
        print("This Is A 3rd Inheritance")

X=A()
X.a()
Y=B()
Y.b()
Z=C()
Z.c()
# print(A.__doc__)
