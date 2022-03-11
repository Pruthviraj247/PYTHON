import matplotlib.pyplot as plt

W = [1,5,6,9,10]
X = [4,6,4,5,6]
Y = [8,5,1,4,4]
Z = [6,9,7,4,1]

plt.plot(W,X,label="Line 1",color="aqua")
plt.plot(Y,Z,label="Line 2",color="gold")
plt.title("This Is A Title")
plt.legend()
plt.show()
