def prime():
    N = int(input("Enter A number"))
    if N<2:
        print("Not A Prime")
    else:
        for i in range(2,N):
            if N%i==0:
                print("Not Prime Number")
                break
        else:
            print("Prime Number")

def even():
    N = int(input("Enter A Number"))
    if N%2==0:
        print("This Is Even Number",N)

    else:
        print("This Is Odd Number",N)

prime()
even()
