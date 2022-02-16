N = int(input("Enter A Number"))

if N<2:
    print("Not Prime")
else:
    for i in range(2,N):
        if N%i==0:
            print("Not A Prime")
    else:
        print("Prime Number")

