import matplotlib.pyplot as plt

Time = [9,7,5,3,2]

label = ["Python","Javascript","Java","C++","Rust"]

plt.pie(Time,labels=label)

plt.title("This Is A PIE Chart")
plt.show()
