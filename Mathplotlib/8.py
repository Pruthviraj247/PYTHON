import matplotlib.pyplot as plt

X = [2,4,6,8,10,12,3,5,7,9]
Y = [1,3,5,7,11,6,4,8,2,9]

plt.scatter(X,Y, label="Label")
plt.title("This Is A Title")
plt.xlabel("This Is A X Label")
plt.ylabel("This Is A Y Label")
plt.legend()
plt.show()
