def fun():
    while True:
        N = int(input("Enter A Number"))
        if N<20:
            print("Done")
            break
        else:
            print("Try Again")
            continue

fun()
print("End of 1st Function")
fun()
