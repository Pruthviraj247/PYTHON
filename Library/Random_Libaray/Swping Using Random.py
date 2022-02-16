from colorama import *
from random import *

Num = randint(1,49)
print(Fore.LIGHTCYAN_EX)

Num1 = randint(50,100)
print(Fore.LIGHTCYAN_EX)

print(Fore.MAGENTA)
print("Before Swapping")
print(Fore.LIGHTYELLOW_EX)
print(Num,Num1)

Num,Num1 = Num1,Num

print(Fore.MAGENTA)
print("After Swapping")
print(Fore.LIGHTGREEN_EX)
print(Num,Num1)

