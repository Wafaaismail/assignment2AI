import csv

import inline as inline
import matplotlib
import array as ar
import pandas as pd
import matplotlib.pyplot as plt
import statistics
import numpy as np


plt.rcParams["figure.figsize"] = (20.0 , 10.0)


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
#print(x1)
#data.head()
x =[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13]

#calc mean
def calcmean(x):
    mean_x =np.mean(x)
    return mean_x

mean_y = np.mean(y)

#calcilate values of m and c as y= mx +c

def estimateCofficents(x,y):
    num = 0
    denom = 0
    for i in range(len(y)):
        num += (x[i] -calcmean(x))*(y[i]-mean_y)
        denom+=(x[i]-calcmean(x))**2
    m = num/denom
    return m

#c= mean_y - (calcmean(x) *estimateCofficents(x,y))


c =(mean_y -(calcmean(x1) *estimateCofficents(x1,y)))
-(mean_y -(calcmean(x2) *estimateCofficents(x2,y)))
-(mean_y -(calcmean(x3) *estimateCofficents(x3,y)))
-(mean_y -(calcmean(x4) *estimateCofficents(x4,y)))
-(mean_y -(calcmean(x5) *estimateCofficents(x5,y)))
-(mean_y -(calcmean(x6) *estimateCofficents(x6,y)))
-(mean_y -(calcmean(x7) *estimateCofficents(x7,y)))
-(mean_y -(calcmean(x8) *estimateCofficents(x8,y)))
-(mean_y -(calcmean(x9) *estimateCofficents(x9,y)))
-(mean_y -(calcmean(x10) *estimateCofficents(x10,y)))
-(mean_y -(calcmean(x11) *estimateCofficents(x11,y)))
-(mean_y -(calcmean(x12) *estimateCofficents(x12,y)))
-(mean_y -(calcmean(x13) *estimateCofficents(x13,y)))

print("c",c)

#print cofficent
coff =[]
for i in range (13):
    coff=estimateCofficents(x[i],y)
    print("cofficent B", coff)

y_predict =c+(x1 *estimateCofficents(x1,y))
+(x2 *estimateCofficents(x2,y))
+(x3 *estimateCofficents(x3,y))
+(x4 *estimateCofficents(x4,y))
+(x5 *estimateCofficents(x5,y))
+(x6 *estimateCofficents(x6,y))
+(x7 *estimateCofficents(x7,y))
+(x8 *estimateCofficents(x8,y))
+(x9 *estimateCofficents(x9,y))
+(x10 *estimateCofficents(x10,y))
+(x11 *estimateCofficents(x11,y))
+(x12 *estimateCofficents(x12,y))
+(x13 *estimateCofficents(x13,y))
print("ypredict",y_predict)

