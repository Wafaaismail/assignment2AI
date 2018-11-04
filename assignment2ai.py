import csv

import inline as inline
import matplotlib
import array as ar

import np as np
import pandas as pd
import statistics
import numpy as np

# #Reading Data
data = pd.read_csv("Boston .csv")
#input values
x1 = data["crim"].values
x2 =data["zn"].values
x3 =data["indus"].values
x4 =data["chas"].values
x5 =data["nox"].values
x6 =data["rm"].values
x7 =data["age"].values
x8 =data["dis"].values
x9 =data["rad"].values
x10 =data["tax"].values
x11 =data["ptratio"].values
x12 =data["black"].values
x13 =data["lstat"].values

y = data["medv"].values

x =[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13]
mean_x =[]
#calc mean of x
def calcmean(x):
    for i in range(13):
        mean_x.append(np.mean(x[i]))
    return mean_x

calcmean(x)
mean_y = np.mean(y)

#calcilate values of m and c as y= mx +c

target =[]
m=[]
mean =[]
def estimateCofficents(x,y):
    num = 0
    denom =0
    for i in range(13):
        target.append(x[i])
        mean.append(mean_x[i])
        for j in range (len(target)):
            b= sum((target[j] - mean[j]) * (y[i] - mean_y))/sum((target[j] - mean[j]) ** 2)
        m.append(b)
    return m
c=0
estimateCofficents(x,y)
for i in range (13):
    c=np.subtract(mean_y,(mean_x[i]*m[i]))

print("c",c)


print(" m " ,m)
