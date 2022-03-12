import matplotlib.pyplot as plt


Time = [9,7,2,5,3]

label = ["Python","Javascript","Java","C++","Rust"]

plt.pie(Time,labels=label, autopct="%0.1f%%", explode=(0.1,0,0,0,0))

plt.title("This Is A PIE Chart")
plt.show()
