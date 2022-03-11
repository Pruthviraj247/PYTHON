import matplotlib.pyplot as plt

Age = [2,4,5,9,12,19,24,28,31,35,38,49,51,56,50,59,63,69,73,70,89,96]

id = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(Age,id, histtype="bar",rwidth=.5)

plt.title("This Is A Title")
plt.xlabel("This Is A X Label")
plt.ylabel("This Is A Y Label")
plt.show()


