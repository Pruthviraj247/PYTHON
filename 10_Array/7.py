from array import *
Stu_roll = array('i', [501,502,503,504,505])
N = len(Stu_roll)
for i in range(N):
    print(i,"=",Stu_roll[i])

print("________________________________________________")
X = Stu_roll[1:5]
for Y in X:
    print(Y)