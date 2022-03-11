import matplotlib.pyplot as plt

Day = [1,2,3,4,5,6,7]

Sleep = [10,7,8,9,11,12,10]
Work = [1,7,4,5,6,4,8]
Class = [2,3,2,4,1,5,1]
Coding = [1,5,3,4,2,1,3]

plt.stackplot(Day,Sleep,Work,Class,Coding, labels=['Sleep','Work','Class','Study'])

plt.title("This Is A Title")
plt.xlabel("This Is A X Label")
plt.ylabel("This Is A Y Label")

plt.legend()
plt.show()


