from colorama import *
from random import *

Num = randint(1,14)
print(Num)

if Num%2==0:
    print(Fore.LIGHTGREEN_EX)
    print("This Number Is Even")
else:
    print(Fore.LIGHTRED_EX)
    print("This Number Is odd")
