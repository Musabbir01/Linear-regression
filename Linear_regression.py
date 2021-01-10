
import math
import csv
import matplotlib.pyplot as plt
data1 = list(csv.reader(open("train.csv")))
data2 = list(csv.reader(open("test.csv")))
test_Set=[]
train_Set=[]
for i in range(0,1001):
    train_Set.append(data1[i])


for i in range(0,301):
    test_Set.append(data2[i])


x_bar=0.0
y_bar=0.0

for i in range(1,1001):
    x_bar+=float(train_Set[i][0])
mean_X=float(x_bar/1000)

for i in range(1,1001):
    y_bar+=float(train_Set[i][1])
mean_Y=float(y_bar/1000)


SSxy=0.0
SSxx=0.0


for i in range(1,1001):
    SSxy+=float((float(float(train_Set[i][0])-float(x_bar)))*(float(float(train_Set[i][1])-float(y_bar))))
for i in range(1,1001):
   SSxx+=math.pow((float(train_Set[i][0])-float(x_bar)),2)

B1=(float(SSxy)/float(SSxx))

B0=float(y_bar)-float(float(B1)*float(x_bar))

print(B1)
print(B0)

List_y=[]
List_x=[]
for i in range(1,301):
   y=float(B0)+(float(B1)*float(test_Set[i][0]))
   List_y.append(y)
   List_x.append(float(test_Set[i][0]))


Err=0.0
List_of_Err=[]
Given_y=[]
for i in range(1,301):
    Given_y.append(test_Set[i][1])

for i in range(0,300):
    Err=float(List_y[i])-float(Given_y[i])
    List_of_Err.append(Err)

Error_sqr_list=[]
for i in range(0,300):
    sq=float(List_of_Err[i])*float(List_of_Err[i])
    Error_sqr_list.append(sq)
print("List of error sqr:")
print(Error_sqr_list)

mean_sqrd_err=0.0
Total_Error=0.0
for i in range(0,300):
    Total_Error+=float(Error_sqr_list[i])
mean_sqrd_err=float(Total_Error)/float(2*300)
print("mean squared error:")
print(mean_sqrd_err)

print(List_x)
print(List_y)
print(Given_y)

x=List_x
y1=List_y
y2=Given_y
plt.scatter(x, y1,c="r",s=2,label="xVSy1")
plt.scatter(x, y2,c="b",s=2,label="xVSy2")
plt.legend()
plt.show()












