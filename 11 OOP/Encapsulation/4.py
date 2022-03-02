class uni:
    def __init__(self):
        self.__maxset = 60

    def set(self):
        print("Maximun Set For CS:",self.__maxset)

    def CS(self,sets):
        self.__maxset = sets

X = uni()
X.set()

X.__maxset = 100
X.set()

X.CS(120)
X.set()

