def primeeven():
    N = int(input("Enter A Number"))
    if N<2:
        print(N,"This Is Not A Prime")
    else:
        for i in range(2,N):
            if N%i==0:
                print(N,"This Is Not Prime Number")
                break
        else:
            print(N,"This Is Prime Number")

    if N%2==0:
        print(N,"This Number Is Even")
    else:
        print(N,"This Number Is Odd")
        
primeeven()
