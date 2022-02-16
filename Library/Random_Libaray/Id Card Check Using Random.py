from colorama import *
from random import *

print(Fore.LIGHTCYAN_EX)
print("|---------------For I'd Card Age Checking Program Using Random Module--------------------|")

Num = randint(1,100)
print(Fore.LIGHTMAGENTA_EX)
print(Num)

if Num==18:
    print(Fore.LIGHTYELLOW_EX)
    print("Please Come To office")

elif Num<18:
    print(Fore.LIGHTRED_EX)
    print("Sorry You  are Not Able")

elif Num<100:
    print(Fore.LIGHTGREEN_EX)
    print("Congrats You Able")

else:
    print(Fore.LIGHTRED_EX)
    print("Sorry You Not")
