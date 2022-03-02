class uni:
    def btech(self,sub):
        print("Your Btech Subject Is:",sub)

    def __fees(self,fee):
        print("Your fess Are:",fee)

    def showfees(self):
        self.__fees(600000)

UNI = uni()
UNI.btech("CS")
UNI.showfees()
UNI.__fees(500000)


