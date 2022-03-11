import matplotlib.pyplot as plt

X = [1,3,5,7,9]
Y = [1,4,5,6,8]

plt.bar(X,Y,label="Line 1",color="lime")
plt.title("This Is A Title")
plt.xlabel("This Is A X Label")
plt.ylabel("This Is A Y Label")
plt.legend()
plt.show()
