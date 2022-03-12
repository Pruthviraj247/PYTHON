from colorama import Fore

print(Fore.CYAN)
print("*************************     Welcome To Domino's     *******************************")
print(Fore.LIGHTWHITE_EX)
print("Choice Your Pizza")

List1 = {"1":"The Unthinkable Pizza Price: 499",
         "2":"Veg Extravaganza Price: 299",
         "3":"Mexican Green Wave Price: 899",
         "4":"Chicken Dominator Price: 599",
         "5":"Chicken Pepperoll Price: 459",
         "6":"Chicken Flesta Price:299"}
print(Fore.MAGENTA)
print(List1)
print(Fore.LIGHTYELLOW_EX)
Choice = input("Enter Your Choice\n")

if Choice not in List1:
    print(Fore.LIGHTRED_EX)
    print("Sorry You Entered Choice Not In Domino's")

else:
    print(Fore.LIGHTGREEN_EX)
    print("Thank You For You Entered Choice: ", List1[Choice])
    print("Your Oder Will Be Deliver Soon")
print(Fore.LIGHTWHITE_EX)
print("Do You What Coke ?")
print("1 For Coke")
print("2 For Quit")
Coke = int(input("Enter Your Choice"))

if(Coke==1):
    print(Fore.LIGHTGREEN_EX)
    print("Thank You Coke Will Be Added")
elif(Coke==2):
    print(Fore.LIGHTYELLOW_EX)
    print("Thank You ")
else:
    print(Fore.LIGHTRED_EX)
    print("Invalid Input")
print(Fore.LIGHTGREEN_EX)
print("Your Oder Will Be Deliver Soon")
