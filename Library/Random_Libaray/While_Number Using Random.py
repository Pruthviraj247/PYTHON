from colorama import *
from random import *

Num = randint(1,15)
print(Fore.LIGHTMAGENTA_EX)
print(Num)

while(True):
    if Num+1<=30:
        Num = Num+1
        print(Fore.LIGHTGREEN_EX)
        print(Num,end="")