import numpy as np
import pandas as pd
data=pd.read_csv("fish.csv")
p=data.isnull().any()
print(data)
print(p)
q=data["Species"].unique()
print(q)
x=data.iloc[:,[0,2,3,4,5,6]].values
y=data.iloc[:,1].values
print(x)
print(y)
print("b4",x.shape)
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct=ColumnTransformer([("encoder",OneHotEncoder(),[0])],remainder="passthrough")
x=ct.fit_transform(x)
print(x)
print(x.shape)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
from sklearn.linear_model import LinearRegression
mlr=LinearRegression()
mlr.fit(x_train,y_train)
ypred=mlr.predict(x_test)
print(ypred)
print(y_test)
print(x_test)
from sklearn.metrics import r2_score
accuracy=r2_score(ypred,y_test)
print(accuracy)
k=mlr.predict(ct.transform([["Bream",24,25,25,11,9]]))
print(k)