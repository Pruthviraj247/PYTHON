def fun1(x):
    return lambda y: y*x
dul = fun1(3)
print(dul(11))