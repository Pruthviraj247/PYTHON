from colorama import *
from random import *

print(Fore.LIGHTCYAN_EX)
print("|----------Prime Number Checking Program Using Random Module--------------|")

Num = randint(1, 10)
print(Fore.MAGENTA)
print(Num)

if Num < 2:
    print(Fore.RED)
    print("Not Prime Number")
else:
    for X in range(2, Num):
        if Num % X == 0:
            print(Fore.RED)
            print("Not A Prime Number")
            break
    else:
        print(Fore.GREEN)
        print("Prime Number")
