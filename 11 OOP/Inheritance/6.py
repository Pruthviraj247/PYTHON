class laptop():
    """This Is Program of Hierarchical Inheritance"""
    def __init__(self,processor,ram,storage):
        self.processor=processor
        self.ram=ram
        self.storage=storage
    def Lappy(self):
        print("This Is A Laptop")

Laptop=laptop(5,8,1)
# Laptop.ram()

Laptop.Lappy()
dir(laptop)
print(dir(laptop))
