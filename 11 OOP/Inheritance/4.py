class A():
    """This Is Program of Multilevel Inheritance """
    def a(self):
        print("This Is A 1st Inheritance")
    def getData(self):
        print("This Is Data of Class A")

class B():
    def b(self):
        print("This Is A 2nd Inheritance")
    def getData(self):
        print("This Is Data of Class B")

class C(B,A):
    def c(self):
        print("This Is A 3rd Inheritance")

X=C()
X.getData()
# X.getData()
print(A.__doc__)
