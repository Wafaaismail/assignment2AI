import csv
import matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


plt.rcParams["figure.figsize"] = (20.0 , 10.0)
# #Reading Data
data = pd.read_csv("Boston .csv")
y = data["medv"].values
x=data["age"].values

#print(data)
data.head()

#mean values

mean_x =np.mean(x)
mean_y =np.mean(y)

#cofficinet calc
num=0
denom=0
for i in range(len(x)):
    num+=(x[i]-mean_x)*(y[i]-mean_y)
    denom+=(x[i]-mean_x)**2

m=num/denom

c=mean_y-(m*mean_x)

print("cofficents are m ,c",m,c)

#plot
max_x =np.max(x)+100
min_x=np.min(x)-100
X =np.linspace(min_x,max_x,100)
Y= c + X*m
plt.scatter(x,y,c="#ef5423",label="Scatter Plot")
plt.plot(X,Y,color="#58b970",label="Regression line")

plt.xlabel("Age")
plt.ylabel("medv")
plt.legend()
plt.show()