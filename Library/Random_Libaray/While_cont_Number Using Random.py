from colorama import *
from random import *

Num = randint(1,100)
print(Num)

while(True):
    if Num<50:
        print(Fore.LIGHTGREEN_EX)
        print("Congress You Number Is Correct")
        break
    else:
        print(Fore.RED)
        print("Sorry Your No Is Wrong")
        continue
