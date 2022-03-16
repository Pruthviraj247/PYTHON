class A():
    """This Is Program of Multiple Inheritance"""
    def a(self):
        print("This Is A 1st Inheritance")

class B():
    def b(self):
        print("This Is A 2nd Inheritance")

class C(A,B):
    def c(self):
        print("This Is A 3rd Inheritance")

X=C()
X.a()
X.b()
# print(A.__doc__)
